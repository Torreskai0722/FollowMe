#!/usr/bin/env python2

import threading
from chip_bldc_driver.msg import Command, Feedback
import sys, select, termios, tty
import math,time
from math import sin, cos, pi, sqrt

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, TwistStamped, Vector3

import message_filters
from sensor_msgs.msg import Image, CameraInfo

import numpy as np

def main():

    rospy.init_node('latency_publisher')

    twist_pub = rospy.Publisher("/latency/twist", TwistStamped, queue_size=10)

    r = rospy.Rate(50)
    while not rospy.is_shutdown():
        ts = TwistStamped()
        ts.twist.linear.x = 1.5
        ts.twist.angular.z = 0.5

        ts.header.frame_id = "map"
        ts.header.stamp = rospy.Time.now()

        twist_pub.publish(ts)

        r.sleep()

if __name__ == '__main__':
    main()
