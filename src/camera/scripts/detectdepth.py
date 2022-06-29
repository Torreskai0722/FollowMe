#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi

import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

lastImage = Image()
def onImage(img):
    global lastImage
    lastImage = img

def onDetection(detection):
    cv_image = bridge.imgmsg_to_cv2(lastImage, desired_encoding='passthrough')
    

    for obj in detection.detections:
        bbox = obj.bbox
        center = bbox.center
        
        start_point = (int(center.x - (bbox.size_x/2)), int( center.y - (bbox.size_y/2)))
        end_point = (int(center.x + (bbox.size_x/2)), int(center.y + (bbox.size_y/2)))

        cv_image = cv2.rectangle(cv_image, start_point, end_point, (255, 0, 0), 5)

    image_message = bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
    pub.publish(image_message)

if __name__ == "__main__":
    rospy.init_node("depthdetector")

    rospy.Subscriber("/camera/color/image_raw", Image, onImage)
    rospy.Subscriber("/detectnet/detections", Detection2DArray, onDetection)
    
    pub = rospy.Publisher("/depthdetector/boundingboximg", Image, queue_size=5)
    
    print("callbacks registered")

    rospy.spin()
       
