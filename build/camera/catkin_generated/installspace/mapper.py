#!/usr/bin/env python 

from __future__ import print_function
from time import time
from math import pi, ceil

import rospy

from geometry_msgs.msg import Vector3, Point32
from sensor_msgs.msg import PointCloud, Image, ChannelFloat32

heading = Vector3()
mapCloud = PointCloud()

def onCameraUpdate(image):
    s = set()
    for i in range(0, len(image.data), 2):
        x = i % (image.width)
        y = ceil(i / (2 * image.height))

        s.add(image.data[i])
        #pt = Point32()
        #pt.x = x
        #pt.y = y
        #latestPointList.append(
        # print("X: " + str(x) + ", Y: " + str(y))
    print(s)


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

        heading = update

if __name__ == "__main__":
    rospy.init_node("mapper")

    rospy.Subscriber("/heading", Vector3, onHeadingUpdate)
    rospy.Subscriber("/camera/depth/image_rect_raw", Image, onCameraUpdate)

    pub = rospy.Publisher("/mapcloud", PointCloud, queue_size=1)
    
    r = rospy.Rate(30)
    while not rospy.is_shutdown():
        pub.publish(mapCloud)
        r.sleep()
