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

import message_filters
from sensor_msgs.msg import Image, CameraInfo

import numpy as np
br_fb = 0
fl_fb = 0
fr_fb = 0
bl_fb = 0

scale = 0.076 * 3.1415926 / 120
lx = 0.245
ly = 0.2

x = 0.0
y = 0.0
th = 0.0

x_stack = [0.0, 0.0]
y_stack = [0.0, 0.0]
th_stack = [0.0, 0.0]

gear_ratio = 20

#odom_broadcaster = None
#odom_pub = None

def update_br_feedback(msg):
    global br_fb
    br_fb = msg.motor_rpm_feedback

def update_fl_feedback(msg):
    global fl_fb
    fl_fb = msg.motor_rpm_feedback * -1

def update_fr_feedback(msg):
    global fr_fb
    fr_fb = msg.motor_rpm_feedback

def update_bl_feedback(msg):
    global bl_fb
    bl_fb = msg.motor_rpm_feedback * -1

def update_Command(fl, br, bl, fr):
    global br_fb
    global fl_fb
    global fr_fb
    global bl_fb
    
    errors = np.array([abs(br.motor_command - br_fb), abs(fl.motor_command * -1 - fl_fb), abs(fr.motor_command - fr_fb), abs(bl.motor_command * -1 - bl_fb)])

    sum_error = np.sum(errors)
    std_error = np.std(errors)
    #print('{},{},{}'.format(1, sum_error, std_error))

def update_feedback(fl, br, bl, fr):
    global last_time
    global x
    global y
    global th
    global odom_broadcaster
    global odom_pub
    
    global br_fb
    global fl_fb
    global fr_fb
    global bl_fb

    global x_stack
    global y_stack
    global th_stack
    print("****************************************************************************************")
    print('[Time], front_left:{}, front_right:{}, back_left:{}, back_right:{}'.format(fl.header.stamp, fr.header.stamp, bl.header.stamp, br.header.stamp))


    br_fb = 1.0 * br.motor_rpm_feedback / gear_ratio
    fl_fb = 1.0 * fl.motor_rpm_feedback * -1 / gear_ratio
    fr_fb = 1.0 * fr.motor_rpm_feedback / gear_ratio
    bl_fb = 1.0 * bl.motor_rpm_feedback * -1 / gear_ratio


    current_time = rospy.Time.now()
    dt = (current_time - last_time).to_sec()
    print('feed back, front_left:{}, front_right:{}, back_left:{}, back_right:{}'.format(fl_fb, fr_fb, bl_fb, br_fb))
    vx = (fl_fb + fr_fb) * scale
    vy = (-fl_fb + fr_fb) * scale
    vth = (-fl_fb + fr_fb) * scale / (lx + ly)
    #vth = (-fl_fb + fr_fb - bl_fb + br_fb) * scale / sqrt(lx*lx + ly*ly)
    
    print('rpm estimation, vx:{}, vy:{}, vth:{}'.format(vx, vy, vth))

    del x_stack[0]
    del y_stack[0]
    del th_stack[0]

    x_stack.append(vx)
    y_stack.append(vy)
    th_stack.append(vth)

    vx = sum(x_stack) / 2.0
    vy = sum(y_stack) / 2.0
    vth = sum(th_stack) / 2.0

    dx = (vx * cos(th) - vy * sin(th)) * dt
    dy = (vx * sin(th) + vy * cos(th)) * dt
    dth = vth * dt

    print('rpm estimation, dx:{}, dy:{}, dth:{}'.format(dx, dy, dth))

    x += dx
    y += dy
    th += dth

    print('rpm estimation, x:{}, y:{}, th:{}'.format(x, y, th))
    

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

    rospy.init_node('Donkey_odometer')

    odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
    odom_broadcaster = tf.TransformBroadcaster()

    # subscribe to the feedback to retrieve current RPM of motor
    # 1:back_right, 2:front_left, 3:front_right, 4:back_left
    # rospy.Subscriber("/bldc_driver_node1/feedback", Feedback, update_fl_feedback)
    # rospy.Subscriber("/bldc_driver_node2/feedback", Feedback, update_br_feedback)
    # rospy.Subscriber("/bldc_driver_node3/feedback", Feedback, update_bl_feedback)
    # rospy.Subscriber("/bldc_driver_node4/feedback", Feedback, update_fr_feedback)

    fl_sub = message_filters.Subscriber("/donkey_bldc_driver_nodeFL/feedback", Feedback)
    br_sub = message_filters.Subscriber("/donkey_bldc_driver_nodeBR/feedback", Feedback)
    bl_sub = message_filters.Subscriber("/donkey_bldc_driver_nodeBL/feedback", Feedback)
    fr_sub = message_filters.Subscriber("/donkey_bldc_driver_nodeFR/feedback", Feedback)

    #fl_command_sub = message_filters.Subscriber("/bldc_driver_node1/Command", Command)
    #br_command_sub = message_filters.Subscriber("/bldc_driver_node2/Command", Command)
    #bl_command_sub = message_filters.Subscriber("/bldc_driver_node3/Command", Command)
    #fr_command_sub = message_filters.Subscriber("/bldc_driver_node4/Command", Command)

    ts = message_filters.ApproximateTimeSynchronizer([fl_sub, br_sub, bl_sub, fr_sub], 20, 0.1)
    #ts_command = message_filters.ApproximateTimeSynchronizer([fl_command_sub, br_command_sub, bl_command_sub, fr_command_sub], 20, 0.1)
    ts.registerCallback(update_feedback)
    #ts_command.registerCallback(update_Command)
    last_time = rospy.Time.now()
    rospy.spin()

if __name__ == '__main__':
    main()
