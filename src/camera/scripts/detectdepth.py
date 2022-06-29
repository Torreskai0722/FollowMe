#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi
import numpy as np

import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

lastImage = Image()
lastDepth = Image()

def onDepth(depth):
    global lastDepth
    lastDepth = depth

def onImage(img):
    global lastImage
    lastImage = img

def getDepthInfoForImage(start_point, end_point, center):
    if lastDepth == Image():
        return 0

    depth_image = bridge.imgmsg_to_cv2(lastDepth, lastDepth.encoding)
    
    #this commented portion works, but it is slow
    #min_depth = 100000000000000
    #max_depth = -1000000000000
    #min_depth_point = (0, 0)
    #max_depth_point = (0, 0)

    #shape = depth_image.shape

    #for i in range(start_point[0] - 1, end_point[0] - 1):
    #    for j in range(start_point[1] - 1, end_point[1] - 1):
    #        
    #        x = int(max(0, min(i, shape[0]-1)))
    #        y = int(max(0, min(j, shape[1]-1)))
    #
    #        depth = depth_image[x, y]
    #
    #        if (depth < min_depth):
    #            min_depth = depth
    #            min_depth_point = (i, j)
    #        elif (depth > max_depth):
    #            max_depth = depth
    #            max_depth_point = (i, j)
    
    cx = int(max(0, min(center.x, depth_image.shape[0]-1)))    
    cy = int(max(0, min(center.y, depth_image.shape[1]-1)))    

    center_depth = depth_image[cx, cy]
    return center_depth
    #return (center_depth, min_depth, max_depth, min_depth_point, max_depth_point)

def onDetection(detection):
    cv_image = cv2.cvtColor(bridge.imgmsg_to_cv2(lastImage, desired_encoding='passthrough'), cv2.COLOR_BGR2RGB)
    
    print('detect')

    for obj in detection.detections:
        bbox = obj.bbox
        center = bbox.center
        
        start_point = (int(center.x - (bbox.size_x/2)), int( center.y - (bbox.size_y/2)))
        end_point = (int(center.x + (bbox.size_x/2)), int(center.y + (bbox.size_y/2)))

        depth_info = getDepthInfoForImage(start_point, end_point, center)

        # bounding box
        cv_image = cv2.rectangle(cv_image, start_point, end_point, (255, 0, 0), 5)
        
        # center point
        cp = (int(center.x), int(center.y))
        
        cv_image = cv2.circle(cv_image, cp, 5, (0, 255, 0), -1)
        cv_image = cv2.putText(cv_image, str(depth_info) + " mm", cp, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # text
        text = str(obj.results[0].id) + ", " + str(round(obj.results[0].score, 2)) + "%"
        text_loc = (start_point[0], start_point[1] - 20)

        cv_image = cv2.putText(cv_image, text, text_loc, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


    image_message = bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
    pub.publish(image_message)


if __name__ == "__main__":
    rospy.init_node("depthdetector")

    rospy.Subscriber("/camera/color/image_raw", Image, onImage)
    rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, onDepth)
    rospy.Subscriber("/detectnet/detections", Detection2DArray, onDetection)

    pub = rospy.Publisher("/depthdetector/boundingboximg", Image, queue_size=5)
    
    print("callbacks registered")

    rospy.spin()
       
