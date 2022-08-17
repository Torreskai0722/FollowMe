#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32
from visualization_msgs.msg import Marker, MarkerArray

MAX_DRIVE = 1.25
TOLERANCE_METERS = 0.1 

move_distance = 0
has_target = False
distance_target = 0
starting_point = [0, 0]
last_error = 0
accum_error = 0

kP = 1.2
kI = 0.0
kD = 0.0

doneiters = 0

def updatePID():
    global distance_target
    global has_target
    global move_distance
    global last_error
    global accum_error
    global doneiters
    
    error = distance_target - move_distance
 
    p = error
    i = error + accum_error 
    d = error - last_error 

    if abs(error) < (TOLERANCE_METERS) and abs(d) < TOLERANCE_METERS:
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
        pid_out = max(min(kP*p + kI*i + kD*d, MAX_DRIVE), -MAX_DRIVE) 
    
        print("error is " + str(error) + ", pid out is " + str(pid_out))

        drive(pid_out, 0)

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
    global distance_target
    global starting_point
    global has_target

    print("got target distance " + str(target.data))
    status_pub.publish(1.0)

    distance_target = target.data
    has_target = True
    starting_point = None

def onOdometryUpdate(odometry):
    global move_distance
    global starting_point

    p = odometry.pose.position

    if starting_point == None:
        if not has_target:
           return 
        starting_point = [p.x, p.y]

    move_distance = math.copysign(1, distance_target) * math.hypot(p.x - starting_point[0], p.y - starting_point[1]) 

    if has_target:
        updatePID()

def stop_holding(msg):
    global has_target
    global reached
    has_target = False
    reached = False
    starting_point = None

# Starting point of the code
if __name__ == "__main__":
    rospy.init_node("follower_drive_controller")

    command_pub = rospy.Publisher("/follower/cmd_vel", Twist, queue_size=10)
    status_pub = rospy.Publisher("/follower/motion_handler/status", Float32, queue_size=10)
    cut_power_pub = rospy.Publisher("/follower/motors/cut_power", Float32, queue_size=10)

    rospy.Subscriber("/follower/follower_pose", PoseStamped, onOdometryUpdate)
    rospy.Subscriber("/follower/drive_command", Float32, onTarget)
    rospy.Subscriber("/follower/motion_handler/quit", Float32, stop_holding)
    
    rospy.spin()
