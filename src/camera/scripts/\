#!/usr/bin/env python 

from __future__ import print_function
from time import time
from math import pi, ceil
import numpy as np

import rospy

from geometry_msgs.msg import Vector3, Point32
from sensor_msgs.msg import PointCloud2, Image, ChannelFloat32

heading = Vector3()
mapCloud = PointCloud2()
lastCamPoints = []

def onCameraUpdate(cloud):
    global lastCamPoints 

    arr = np.frombuffer(cloud.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    print(arr)
    
    lastCamPoints = cloud.data

def onHeadingUpdate(update):
    global heading

    # determine if it is a decent change (10 degrees or more)
    dx = abs(update.x - heading.x)
    dy = abs(update.y - heading.y)
    dz = abs(update.z - heading.z)

    if (dx + dy + dz) >= 10:
        # it is a decent change
        # get map and add points to the map
        print("change detected")

        mapCloud.data.extend(lastCamPoints)
        mapCloud.width += len(lastCamPoints)

        heading = update

if __name__ == "__main__":
    rospy.init_node("mapper")

    rospy.Subscriber("/heading", Vector3, onHeadingUpdate)
    rospy.Subscriber("/camera/depth/color/points", PointCloud2, onCameraUpdate)

    pub = rospy.Publisher("/mapcloud", PointCloud2, queue_size=1)
    
    r = rospy.Rate(30)
    while not rospy.is_shutdown():
        pub.publish(mapCloud)
        r.sleep()
