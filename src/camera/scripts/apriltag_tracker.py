#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi
import os
import numpy as np

import rospy
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2
import apriltag

bridge = CvBridge()
detector = apriltag.Detector()

K = np.array([-0.017655, 0.070566, -0.001669, -0.006414, 0])

tag_size = 0.07
ob_pt1 = [-tag_size/2, -tag_size/2, 0.0]
ob_pt2 = [ tag_size/2, - tag_size/2, 0.0]
ob_pt3 = [ tag_size/2,  tag_size/2, 0.0]
ob_pt4 = [-tag_size/2,  tag_size/2, 0.0]
ob_pts = ob_pt1 + ob_pt2 + ob_pt3 + ob_pt4
object_pts = np.array(ob_pts).reshape(4,3)

def estimateTransformToCamera(self, corners_3d, camera_matrix, dist_coeff, rmat, tvec):
        rot_vec=np.array([])
        # is ok?
        rmat=np.array([])
        cv2.solvePnP(corners_3d, self.m_corners, camera_matrix, dist_coeff, rot_vec, tvec)
        cv2.Rodrigues(rot_vec, rmat)
        return rmat
        
def image_process(frame):
    results = detector.detect(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))

    for result in results:
        print(result)
        frame = cv2.circle(frame, (int(result.center[0]), int(result.center[1])), 15, (255, 0, 0), -1)
        
        # H = np.array(result.homography)
        # H /=  H.sum(axis=1)[:,np.newaxis]

        # c1 = H[0]
        # c2 = H[1]
        # c3 = np.cross(c1, c2)

        # T = H[2]

        # print(T)
        # R = [[], [], []]
        # for i in range(0, 3):

        # H = H.T
        # h1 = H[0]
        # h2 = H[1]
        # h3 = H[2]
        # K_inv = np.linalg.inv(K)
        # L = 1 / np.linalg.norm(np.dot(K_inv, h1))
        # r1 = L * np.dot(K_inv, h1)
        # r2 = L * np.dot(K_inv, h2)
        # r3 = np.cross(r1, r2)
        # T = L * (np.dot(K_inv, h3.reshape(3, 1)))
        # R = np.array([[r1], [r2], [r3]])
        # R = np.reshape(R, (3, 3))

        # print("Transform: ")
        # print(T)
        # print("Rotation: ")
        # print(R)

    return frame

def onImage(img):
    cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(img, desired_encoding='passthrough'), cv2.COLOR_BGR2RGB)
    # cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough')
    
    out = image_process(cv_image)
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
       

