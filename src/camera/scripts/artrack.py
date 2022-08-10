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
from detector import find_contours, get_tag_id, get_tag_orientation
from superimpose import get_h_matrices

bridge = CvBridge()

def onImage(img):
    # cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(img, desired_encoding='passthrough'), cv2.COLOR_BGR2RGB)
    cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough')

    rows,cols,channels = cv_image.shape
    contours = find_contours(cv_image)

    # Define array to store max contour area
    max_contour_area = np.zeros((1, 1, 2), dtype=int)
    for contour in contours:

        contour_area = cv2.contourArea(contour)
        contour_poly_curve = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, closed=True), closed=True)
        if 2000 < contour_area < 22600 and len(contour_poly_curve) == 4:
            # Draw the selected Contour matching the criteria fixed
            cv2.drawContours(vf_original, [contour], 0, (0, 0, 225), 1)
            # Warp the video frame
            h_mat, _ = get_h_matrices(contour_poly_curve, ref_dimension, ref_dimension)
            vf_warp = cv2.warpPerspective(cv_image, h_mat, (ref_dimension, ref_dimension))
            vf_warp_gray = cv2.cvtColor(vf_warp, cv2.COLOR_BGR2GRAY)
            # Get orientation and tag ID
            orientation = get_tag_orientation(vf_warp_gray)
            tag_id = get_tag_id(vf_warp_gray, orientation)
            # Display tag ID on each frame
            print(total_frames, orientation, tag_id)
            cv2.putText(cv_image, "Tag ID: " + tag_id, (contour_poly_curve[0][0][0] - 50,
                                                            contour_poly_curve[0][0][1] - 50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225), 2, cv2.LINE_AA)

    image_message = bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
    drawn_pub.publish(image_message)
    

if __name__ == "__main__":
    rospy.init_node("ar_tag_tracker")

    rospy.Subscriber("/usb_cam/image_raw", Image, onImage)
    drawn_pub = rospy.Publisher("/tagtracker/img", Image, queue_size=5)

    rospy.spin()
       
