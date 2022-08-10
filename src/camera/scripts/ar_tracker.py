#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi
import os
import numpy as np

import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

from cv_bridge import CvBridge
import cv2
import copy
import imutils
from detector import find_contours, get_tag_id, get_tag_orientation
from superimpose import get_h_matrices

bridge = CvBridge()

dim = 200
p1 = np.array([
    [0, 0],
    [dim - 1, 0],
    [dim - 1, dim - 1],
    [0, dim - 1]], dtype="float32")

#
def id_decode(image):  # To detect the ID information for the tag
    ret, img_bw = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    corner_pixel = 255
    cropped_img = img_bw[50:150, 50:150]

    (h, w) = cropped_img.shape
    # calculate the center of the image
    center = (w / 2, h / 2)
    # print (h,w)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    found = False
    block_1 = cropped_img[37, 37]
    block_3 = cropped_img[62, 37]
    block_2 = cropped_img[37, 62]
    block_4 = cropped_img[62, 62]
    white = 255
    if block_3 == white:
        block_3 = 1
    else:
        block_3 = 0
    if block_4 == white:
        block_4 = 1
    else:
        block_4 = 0
    if block_2 == white:
        block_2 = 1
    else:
        block_2 = 0
    if block_1 == white:
        block_1 = 1
    else:
        block_1 = 0
    # To get the orientation of the tag
    if cropped_img[85, 85] == corner_pixel:
        return list([block_3, block_4, block_2, block_1]), "BR"
    elif cropped_img[15, 85] == corner_pixel:
        return list([block_4, block_2, block_1, block_3]), "TR"
    elif cropped_img[15, 15] == corner_pixel:
        return list([block_2, block_1, block_3, block_4]), "TL"
    elif cropped_img[85, 15] == corner_pixel:
        return list([block_1, block_3, block_4, block_2]), "BL"

    return None, None


def draw_cube(img, imgpts):  # To draw the cube
    imgpts = np.int32(imgpts).reshape(-1, 2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 255), 3)

    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255, 255, 0), 3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
    return img


def order(pts):  # To get the ordered points in a clockwise direction
    ordered = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    ordered[0] = pts[np.argmin(s)]
    ordered[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    # print(np.argmax(diff))
    ordered[1] = pts[np.argmin(diff)]
    ordered[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return ordered


def homo(p, p1):
    A = []
    p2 = order(p)
    for i in range(0, len(p1)):
        x, y = p1[i][0], p1[i][1]
        u, v = p2[i][0], p2[i][1]
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y, -u])
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y, -v])
    A = np.array(A)
    U, S, V = np.linalg.svd(A)
    l = V[-1, :] / V[-1, -1]
    h = np.reshape(l, (3, 3))
    return h

# Function to calculate Projection matrix
def calculator(h):
    K = np.array(
        [[1406.08415449821, 0, 0], [2.20679787308599, 1417.99930662800, 0], [1014.13643417416, 566.347754321696, 1]]).T
    h = inv(h)
    b_new = np.dot(inv(K), h)
    b1 = b_new[:, 0].reshape(3, 1)
    b2 = b_new[:, 1].reshape(3, 1)
    r3 = np.cross(b_new[:, 0], b_new[:, 1])
    b3 = b_new[:, 2].reshape(3, 1)
    L = 2 / (norm((inv(K)).dot(b1)) + norm((inv(K)).dot(b2)))
    r1 = L * b1
    r2 = L * b2
    r3 = (r3 * L * L).reshape(3, 1)
    t = L * b3
    r = np.concatenate((r1, r2, r3), axis=1)

    return r, t, K


def contour_generator(frame):
    test_img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    test_blur = cv2.GaussianBlur(test_img1, (3, 3), 0)
    edge = cv2.Canny(test_blur, 75, 200)
    edge1 = copy.copy(edge)
    countour_list = list()
    ctrs, h = cv2.findContours(edge1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index = list()
    for hier in h[0]:
        if hier[3] != -1:
            index.append(hier[3])

    for c in index:
        peri = cv2.arcLength(ctrs[c], True)
        approx = cv2.approxPolyDP(ctrs[c], 0.02 * peri, True)

        if len(approx) > 4:
            peri1 = cv2.arcLength(ctrs[c - 1], True)
            corners = cv2.approxPolyDP(ctrs[c - 1], 0.02 * peri1, True)
            countour_list.append(corners)

    new_contour_list = list()
    for contour in countour_list:
        if len(contour) == 4:
            new_contour_list.append(contour)
    final_contour_list = list()
    for element in new_contour_list:
        if cv2.contourArea(element) < 2500:
            final_contour_list.append(element)

    return final_contour_list


def reorient(location, maxDim):
    if location == "BR":
        p1 = np.array([
            [0, 0],
            [maxDim - 1, 0],
            [maxDim - 1, maxDim - 1],
            [0, maxDim - 1]], dtype="float32")
        return p1
    elif location == "TR":
        p1 = np.array([
            [maxDim - 1, 0],
            [maxDim - 1, maxDim - 1],
            [0, maxDim - 1],
            [0, 0]], dtype="float32")
        return p1
    elif location == "TL":
        p1 = np.array([
            [maxDim - 1, maxDim - 1],
            [0, maxDim - 1],
            [0, 0],
            [maxDim - 1, 0]], dtype="float32")
        return p1

    elif location == "BL":
        p1 = np.array([
            [0, maxDim - 1],
            [0, 0],
            [maxDim - 1, 0],
            [maxDim - 1, maxDim - 1]], dtype="float32")
        return p1


def image_process(frame, p1):
    final_contour_list = contour_generator(frame)
    cube_list = list()
    axis = np.float32(
        [[0, 0, 0], [0, 200, 0], [200, 200, 0], [200, 0, 0], [0, 0, -200], [0, 200, -200], [200, 200, -200],
         [200, 0, -200]])
    mask = np.full(frame.shape, 0, dtype='uint8')
    for i in range(len(final_contour_list)):
        cv2.drawContours(frame, [final_contour_list[i]], -1, (0, 255, 0), 2)
        # cv2.imshow("Outline", frame)
        c_rez = final_contour_list[i][:, 0]
        H_matrix = homo(p1, order(c_rez))
        tag = cv2.warpPerspective(frame, H_matrix, (200, 200))

        # cv2.imshow("Outline", frame)
        # cv2.imshow("Tag after homogenous", tag)

        tag1 = cv2.cvtColor(tag, cv2.COLOR_BGR2GRAY)
        decoded, location = id_decode(tag1)
        #empty = np.full(frame.shape, 0, dtype='uint8')
        if not location == None:
            p2 = reorient(location, 200)
            if not decoded == None:
                r, t, K = calculator(H_matrix)
                points, jac = cv2.projectPoints(axis, r, t, K, np.zeros((1, 4)))
                img = draw_cube(mask, points)
                cube_list.append(img.copy())
    if cube_list != []:  # empty cube list
        for cube in cube_list:
            temp = cv2.add(mask, cube.copy())
            mask = temp

        final_image = cv2.add(frame, mask)
    
        return final_image
    print("none to draw")
    return frame

def onImage(img):
    cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(img, desired_encoding='passthrough'), cv2.COLOR_BGR2RGB)
    # cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough')
    
    img = cv2.resize(cv_image, (0, 0), fx=0.5, fy=0.5)
    out = image_process(img, p1)
    # rows,cols,channels = cv_image.shape
    # contours = find_contours(cv_image)

    # # Define array to store max contour area
    # max_contour_area = np.zeros((1, 1, 2), dtype=int)
    # for contour in contours:

    #     contour_area = cv2.contourArea(contour)
    #     contour_poly_curve = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, closed=True), closed=True)
    #     if 2000 < contour_area < 22600 and len(contour_poly_curve) == 4:
    #         # Draw the selected Contour matching the criteria fixed
    #         cv2.drawContours(vf_original, [contour], 0, (0, 0, 225), 1)
    #         # Warp the video frame
    #         h_mat, _ = get_h_matrices(contour_poly_curve, ref_dimension, ref_dimension)
    #         vf_warp = cv2.warpPerspective(cv_image, h_mat, (ref_dimension, ref_dimension))
    #         vf_warp_gray = cv2.cvtColor(vf_warp, cv2.COLOR_BGR2GRAY)
    #         # Get orientation and tag ID
    #         orientation = get_tag_orientation(vf_warp_gray)
    #         tag_id = get_tag_id(vf_warp_gray, orientation)
    #         # Display tag ID on each frame
    #         print(total_frames, orientation, tag_id)
    #         cv2.putText(cv_image, "Tag ID: " + tag_id, (contour_poly_curve[0][0][0] - 50,
    #                                                         contour_poly_curve[0][0][1] - 50),
    #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225), 2, cv2.LINE_AA)

    image_message = bridge.cv2_to_imgmsg(out, encoding="passthrough")
    drawn_pub.publish(image_message)
    

if __name__ == "__main__":
    rospy.init_node("ar_tag_tracker")

    rospy.Subscriber("/usb_cam/image_raw", Image, onImage)
    drawn_pub = rospy.Publisher("/tagtracker/img", Image, queue_size=5)

    rospy.spin()
       

