#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi

import rospy
from sensor_msgs.msg import Image

def onImage(img):
    pub.publish(img)

if __name__ == "__main__":
    rospy.init_node("relay")

    rospy.Subscriber("/camera/color/raw", Image, onImage)

    pub = rospy.Publisher("/ros_deep_learning/video_source", Image, queue_size=1)

    rospy.spin()
       
