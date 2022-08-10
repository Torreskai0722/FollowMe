#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi
import os
import numpy as np

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from vision_msgs.msg import Detection2DArray

from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

lastImage = Image()
lastDepth = Image()

lastDepthReading = 0

def onDepth(depth):
    onLoop(depth)

def getDepthInfoForImage(depth_image, x, y):
    cx = int(max(0, min(x, depth_image.shape[0]-1)))    
    cy = int(max(0, min(y, depth_image.shape[1]-1)))    

    center_depth = depth_image[cx, cy]
    return center_depth
    #return (center_depth, min_depth, max_depth, min_depth_point, max_depth_point)

def onLoop(depth):
    if depth == Image():
        return

    cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(depth, desired_encoding='passthrough'), cv2.COLOR_BGR2RGB)

    w, h, c = cv_image.shape
     
    depth_info = getDepthInfoForImage(cv_image, w/2, h/2)
    lastDepthReading = depth_info
    
    print(depth_info)


if __name__ == "__main__":

    rospy.init_node("distance_reader")

    rospy.Subscriber("/camera/depth/image_rect_raw", Image, onDepth)

    pub = rospy.Publisher("/distancereading", Float32, queue_size=5)
    
    print("callbacks registered")
    
    rospy.spin()
