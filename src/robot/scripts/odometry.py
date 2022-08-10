#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
from time import time

import tf
import rospy

from geometry_msgs.msg import PoseStamped, Vector3, PoseWithCovariance, TwistWithCovariance, Pose, Twist, TransformStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler

lastPose = PoseStamped()
lastTime = 0

pub = rospy.Publisher("odom", Odometry, queue_size=5)

def handle_slam(poseStamped):
    br = tf.TransformBroadcaster()
    global pub
    global lastPose
    global lastTime

    twc = TwistWithCovariance()
    if lastTime != 0:
        dt = time() - lastTime

        dx = lastPose.pose.position.x - poseStamped.pose.position.x
        dy = lastPose.pose.position.y - poseStamped.pose.position.y
        dz = lastPose.pose.position.z - poseStamped.pose.position.z

        dxr = lastPose.pose.orientation.x - poseStamped.pose.orientation.x
        dyr = lastPose.pose.orientation.y - poseStamped.pose.orientation.y
        dzr = lastPose.pose.orientation.z - poseStamped.pose.orientation.z
        dwr = lastPose.pose.orientation.w - poseStamped.pose.orientation.w

        linear = Vector3()
        linear.x = dx/dt
        linear.y = dy/dt
        linear.z = dz/dt

        (roll, pitch, yaw) = euler_from_quaternion((dxr, dyr, dzr, dwr))
        angular = Vector3()
        angular.x = roll/dt
        angular.y = pitch/dt
        angular.z = yaw/dt

        twist = Twist()
        twist.linear = linear
        twist.angular = angular
        twc.twist = twist
    
    pwc = PoseWithCovariance()
    pwc.pose = poseStamped.pose

    odom = Odometry()
    odom.pose = pwc
    odom.twist = twc

    odom_trans = TransformStamped()
    odom_trans.header.frame_id = "odom"
    odom_trans.child_frame_id = "base_link"
    odom_trans.header.stamp = rospy.Time.now()
    
    odom_trans.transform.translation = poseStamped.pose.position
    odom_trans.transform.rotation = poseStamped.pose.orientation
    br.sendTransform((poseStamped.pose.position.x, poseStamped.pose.position.y, poseStamped.pose.position.z), (poseStamped.pose.orientation.x, poseStamped.pose.orientation.y, poseStamped.pose.orientation.z, poseStamped.pose.orientation.w), rospy.Time.now(), "odom", "base_link")
    
    odom.child_frame_id = "base_link"
    odom.header.frame_id = "odom"
    
    pub.publish(odom)

    lastTime = time()
    lastPose = poseStamped
    
        
if __name__ == "__main__":
    rospy.init_node("odometry_handler")
    
    rospy.Subscriber("/slam_out_pose", PoseStamped, handle_slam)

    rospy.spin()
   
