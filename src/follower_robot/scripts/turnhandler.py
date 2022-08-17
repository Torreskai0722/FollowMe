#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32
from visualization_msgs.msg import Marker, MarkerArray

MAX_TURN = 1.25
TOLERANCE_RADIANS = 4 * math.pi/180

robot_yaw = 0
has_target = False
angle_target = 0
last_error = 0
accum_error = 0

kP = 1.1
kI = 0.005
kD = 0.8

doneiters = 0

def angle_bound(yaw):
    return yaw - (2 * math.pi) * math.floor(yaw / (2 * math.pi))

def updatePID():
    global angle_target
    global has_target
    global robot_yaw
    global last_error
    global accum_error
    global doneiters
    
    error = angle_target - robot_yaw
 
    p = error
    i = error + accum_error 
    d = error - last_error 

    if abs(error) < (TOLERANCE_RADIANS) and abs(d) < TOLERANCE_RADIANS:
        if doneiters < 1:
            status_pub.publish(0.0)
            print("Done")
        doneiters += 1
        # cut_power_pub.publish(0.0)
        # drive(0, 0)
        if doneiters >= 8:
            doneiters = 0
            last_error = 0
            accum_error = 0
    else: 
        pid_out = max(min(kP*p + kI*i + kD*d, MAX_TURN), -MAX_TURN) 

        print("error is " + str(error) + ", pid out is " + str(pid_out))
        
        drive(0, pid_out)
        
        accum_error = i
        last_error = error

def drive(forward, turning):
    twist = Twist()
    linear = Vector3()
    linear.x = forward 
    angular = Vector3()
    angular.z = turning 

    twist.linear = linear
    twist.angular = angular

    command_pub.publish(twist)

def onTarget(target):
    global angle_target
    global has_target

    status_pub.publish(-1.0)

    angle_target = target.data
    has_target = True

def onOdometryUpdate(odometry):
    global robot_yaw

    o = odometry.pose.orientation
    _, _, yaw = euler_from_quaternion((o.x, o.y, o.z, o.w))

    robot_yaw = angle_bound(yaw)

    if has_target:
        updatePID()

def stop_holding(msg):
    global has_target
    global reached
    has_target = False
    reached = False

# Starting point of the code
if __name__ == "__main__":
    rospy.init_node("follower_turn_controller")

    command_pub = rospy.Publisher("/follower/cmd_vel", Twist, queue_size=10)
    status_pub = rospy.Publisher("/follower/motion_handler/status", Float32, queue_size=10)
    cut_power_pub = rospy.Publisher("/follower/motors/cut_power", Float32, queue_size=10)

    rospy.Subscriber("/follower/follower_pose", PoseStamped, onOdometryUpdate)
    rospy.Subscriber("/follower/turn_command", Float32, onTarget)
    rospy.Subscriber("/follower/motion_handler/quit", Float32, stop_holding)
    
    rospy.spin()
