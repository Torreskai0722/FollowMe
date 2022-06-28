#!/usr/bin/env python 

from __future__ import print_function
from time import time
from math import pi, ceil, sin, cos
import numpy as np
from collections import namedtuple

import rospy

from geometry_msgs.msg import Vector3, Point32
from sensor_msgs.msg import PointCloud2, Image, ChannelFloat32
import sensor_msgs.point_cloud2 as pc2
heading = Vector3()
mapCloud = PointCloud2()
lastCamPoints = []

Point = namedtuple('Point', 'x y z rgb')

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

def rotateByHeading(point):
    # from https://www.mathworks.com/matlabcentral/answers/123763-how-to-rotate-entire-3d-data-with-x-y-z-values-along-a-particular-axis-say-x-axis
    tx = heading.z * (pi/180)
    ty = heading.y * (pi/180)
    tz = heading.x * (pi/180)

    x = point.x
    y = point.y
    z = point.z

    # rotate about x axis
    y = y*cos(tx) - z*sin(tx)
    z = y*sin(tx) + z*cos(tx)

    # rotate about y axis
    x = x*cos(ty) + z*sin(ty)
    z = z*cos(ty) - x*sin(ty)

    # rotate about z axis
    x = x*cos(tz) - y*sin(tz)
    y = x*sin(tz) + y*cos(tz)

    p = Point(x, y, z, point.rgb)
    
    return p 


def onHeadingUpdate(update):
    global heading
    global mapCloud

    # determine if it is a decent change (10 degrees or more)
    dx = abs(update.x - heading.x)
    dy = abs(update.y - heading.y)
    dz = abs(update.z - heading.z)

    if (dx + dy + dz) >= 5:
        # it is a decent change
        # get map and add points to the map
        print("change detected")

        heading = update
        
        if mapCloud != PointCloud2():
            points = pc2.read_points_list(mapCloud)
            for p in lastCamPoints:
                points.append(rotateByHeading(p))
                
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
