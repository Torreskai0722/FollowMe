#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
import math
import numpy as np

from sensor_msgs.msg import LaserScan, PointCloud2
import laser_geometry.laser_geometry as lg
import rospy

def onRecieve(data):
    converted = lp.projectLaser(data)
    pub.publish(converted)


if __name__ == "__main__":
    rospy.init_node("pointcloud_converter")

    lp = lg.LaserProjection()
    pub = rospy.Publisher("filtered_cloud", PointCloud2, queue_size=1)

    rospy.Subscriber("scan", LaserScan, onRecieve)
    rospy.spin()
