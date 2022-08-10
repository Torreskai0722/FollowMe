#!/usr/bin/env python2

import threading
from chip_bldc_driver.msg import Command, Feedback
import sys, select, termios, tty
import math,time
from math import sin, cos, pi, sqrt

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from std_msgs.msg import Float32

import message_filters
from sensor_msgs.msg import Image, CameraInfo

import numpy as np

x = 0
y = 0
th = 0

def update_feedback(right, left):
    global last_time
    global x
    global y
    global th
    global odom_broadcaster
    global odom_pub
    
    current_time = rospy.Time.now()
    dt = (current_time - last_time).to_sec()
    
    deltaLeft = left.data * dt
    deltaRight = right.data * dt

    #if abs(deltaLeft - deltaRight) < 0.01 :
    #    dx = deltaLeft * cos(th)
    #    dy = deltaRight * sin(th)
    #    dth = 0
    #else:
    #    print("turning")
    #    R = 0.49 * (deltaLeft + deltaRight) / (2 * (deltaRight - deltaLeft))
    #    wd = (deltaRight - deltaLeft) / (0.49 * 2.45)
    #    
    #    dx = (R * sin(wd + th) - R * sin(th))
    #    dy = (-R * cos(wd + th) + R * cos(th))
    #    dth = (th + wd)
    #    dth = wd

    ##dth = (deltaLeft - deltaRight) / 0.5

    #th += dth

    #if(th > 6.28):
    #    th -= 6.28
    #elif(th < -6.28):
    #    th += 6.28

    #meanDistance = (deltaLeft + deltaRight)/2
    #dx = meanDistance * cos(th)
    #dy = meanDistance * sin(th)

    #x += dx
    #y += dy

    #th = max(min(th, 2*3.1415926), 2*3.1415926)
    
    vx = (left.data + right.data)
    vy = (-left.data + right.data)
    vth = (-left.data + right.data) 

    vx = vx / 2.0
    vy = vy / 2.0
    vth = vth / 2.0

    dx = (vx * cos(th) - vy * sin(th)) * dt
    dy = (vx * sin(th) + vy * cos(th)) * dt
    dth = vth * dt

    x += dx
    y += dy
    th += dth

    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
    #odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (x, y, 0.),
    #    (0, 0, 0),
        odom_quat,
        current_time,
        # "fakebase_link",
        # "fakeodom",
        "base_link",
        "odom"
    )

    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom" #"fakeodom"

    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))
    #odom.pose.pose = Pose(Point(0, 0, 0.), Quaternion(*odom_quat))

    # set the velocity
    vx = dx / dt
    vy = dy / dt
    vth = dth / dt
    
    odom.child_frame_id = "base_link" #"fakebase_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
    #odom.twist.twist = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time

def main():
    global odom_broadcaster
    global odom_pub
    global last_time

    rospy.init_node('diff_drive_odometer')

    odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
    odom_broadcaster = tf.TransformBroadcaster()

    # 1:back_right, 2:front_left, 3:front_right, 4:back_left
    # rospy.Subscriber("/bldc_driver_node1/feedback", Feedback, update_fl_feedback)
    # rospy.Subscriber("/bldc_driver_node2/feedback", Feedback, update_br_feedback)
    # rospy.Subscriber("/bldc_driver_node3/feedback", Feedback, update_bl_feedback)
    # rospy.Subscriber("/bldc_driver_node4/feedback", Feedback, update_fr_feedback)

    right_sub = message_filters.Subscriber("/drivebase_speeds/right", Float32)
    left_sub = message_filters.Subscriber("/drivebase_speeds/left", Float32)

    ts = message_filters.ApproximateTimeSynchronizer([right_sub, left_sub], 20, 0.1, allow_headerless=True)
    ts.registerCallback(update_feedback)
    last_time = rospy.Time.now()
    rospy.spin()

if __name__ == '__main__':
    main()
