#!/usr/bin/env python 

from __future__ import print_function
from time import time
from math import pi, ceil
import numpy as np

import rospy

from geometry_msgs.msg import Vector3, Point32
from sensor_msgs.msg import PointCloud2, Image, ChannelFloat32
import sensor_msgs.point_cloud2 as pc2

heading = Vector3()
mapCloud = PointCloud2()
lastCamPoints = []

def asArr(cloud):
    if cloud.width == 0:
        return []
    return np.frombuffer(cloud.data, dtype=np.uint8).reshape(cloud.height, cloud.width, -1)

def onCameraUpdate(cloud):
    global lastCamPoints 
    global mapCloud

    lastCamPoints = pc2.read_points_list(cloud)

    if mapCloud == PointCloud2():
        mapCloud = cloud

def onHeadingUpdate(update):
    global heading
    global mapCloud

    # determine if it is a decent change (10 degrees or more)
    dx = abs(update.x - heading.x)
    dy = abs(update.y - heading.y)
    dz = abs(update.z - heading.z)

    if (dx + dy + dz) >= 10:
        # it is a decent change
        # get map and add points to the map
        print("change detected")

        heading = update
        
        if mapCloud != PointCloud2():
            points = pc2.read_points_list(mapCloud)
            for p in lastCamPoints:
                points.append(p)
            if (len(points) > 0):
                mapCloud = pc2.create_cloud(mapCloud.header, mapCloud.fields, points)

        #points = np.hstack([asArr(mapCloud), lastCamPoints]) if len(lastCamPoints) > 0 else asArr(mapCloud)
        
        #mapCloud.data = np.getbuffer(points)
        #mapCloud.width += len(lastCamPoints)

if __name__ == "__main__":
    rospy.init_node("mapper")

    rospy.Subscriber("/heading", Vector3, onHeadingUpdate)
    rospy.Subscriber("/camera/depth/color/points", PointCloud2, onCameraUpdate)

    pub = rospy.Publisher("/mapcloud", PointCloud2, queue_size=1)
    
    r = rospy.Rate(30)
    while not rospy.is_shutdown():
        pub.publish(mapCloud)
        r.sleep()
