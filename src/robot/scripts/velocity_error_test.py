#!/usr/bin/env python2

import threading
from chip_bldc_driver.msg import Command, Feedback
import sys, select, termios, tty
import math,time
from math import sin, cos, pi, sqrt

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, PoseStamped, Quaternion, Twist, Vector3

import message_filters
from sensor_msgs.msg import Image, CameraInfo

import numpy as np

lastTime = 0
lastPoint = [0, 0]
datapoints = []
curV = 0

def onVelocityCommand(twist):
    global curV
    global datapoints
    if curV == 0:
        return
    
    vmag = math.hypot(twist.linear.x, twist.linear.y)
    datapoints.append(curV - vmag)

def onOdometryUpdate(ps):
    global lastTime
    global curV
    global lastPoint
    pose = ps.pose

    if not lastTime == 0:
        dt = rospy.Time.now() - lastTime
        dx = math.hypot(pose.position.x - lastPoint[0], pose.position.y - lastPoint[1])
        curV = dx/dt.to_sec()
    
    lastTime = rospy.Time.now()
    lastPoint = [pose.position.x , pose.position.y]

def main():

    rospy.init_node('velocity_measurement')

    rospy.Subscriber("/cmd_vel", Twist, onVelocityCommand)
    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)

    while not rospy.is_shutdown():
        l = input("input")
        if l:
            print(datapoints)
            np.savetxt("velocity_error.csv", [np.asarray(datapoints)], delimiter=",")
            print("saved to file")

if __name__ == '__main__':
    main()
