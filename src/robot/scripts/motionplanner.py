#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32, String
from visualization_msgs.msg import Marker, MarkerArray

# syntax: [type (0 = drive, 1 = turn), amount (distance in m or angle in r), done (0f 1t)]
actions = [
        # [0.0, 1.0, 0],
        # [1.0, math.pi/2, 0],
        # [0.0, -1.0, 0]
]

remaining_waypoints = [
    # [1.0, 0.0]
]

started_going = False
should_start = False 
cur_pose = [0.0, 0.0, 0.0]

def angle_bound(yaw):
    return yaw - (2 * math.pi) * math.floor(yaw / (2 * math.pi))

def create_actions():
    global actions
    global started_going
    global should_start

    if len(remaining_waypoints) > 0:
        actions = []
        print("calculating next actions")
        next_point = remaining_waypoints[0]
        
        dx = next_point[0] - cur_pose[0]
        dy = next_point[1] - cur_pose[1]
        theta_to_turn = math.atan2(dy, dx)
        distance_target = math.hypot(dx, dy)

        if abs(angle_bound(theta_to_turn) - angle_bound(cur_pose[2])) > 3 * (math.pi / 180):
            turn_action = [1.0, angle_bound(theta_to_turn), 0.0]
            actions.append(turn_action)
        
        drive_action = [0.0, distance_target, 0.0]
        actions.append(drive_action)
        should_start = True
    else:
        print("All waypoints have been reached")
        drive(0, 0)
        quit_pub.publish(0)


def onOdometryUpdate(odometry):
    global actions
    global started_going
    global should_start
    global cur_pose
    global remaining_waypoints

    p = odometry.pose.position
    o = odometry.pose.orientation
    _, _, yaw = euler_from_quaternion((o.x, o.y, o.z, o.w))

    cur_pose = [p.x, p.y, yaw]

    if should_start and not started_going:
        print("starting new actions")
        print(actions)
        should_start = False
        started_going = True

    if not started_going:
        return

    ran_one = False
    
    idx = -1
    for action in actions:
        idx += 1
        if action[2] == 1:
            continue

        ran_one = True

        if action[2] == 0.0:
            action[2] = 0.5
            print("queing next action")
            if action[0] == 0.0:
                #it is a drive command
                drive_pub.publish(action[1])
            else:
                turn_pub.publish(action[1])
        
        if last_status == 0.0:
            # current command finished
            # if not (idx == (len(actions) - 1)):
            quit_pub.publish(0.0)            

            action[2] = 1
            
        break

    if not ran_one:
        # all actions have finished
        # drive(0, 0)
        print("Reached Next Waypoint")

        remaining_waypoints = remaining_waypoints[1:]
        started_going = False
        create_actions()

last_status = -2.0

def onStatusUpdate(msg):
    global last_status

    last_status = msg.data
    print("Got status update of " + str(last_status))

    #status = msg.data
    # a command finished
    '''if status == 0.0:
        braked = False
        for action in actions:
            if action[2] == 0:
                action[2] = 1
                braked = True
                break
        if braked = False:
            print("Done with all actions")
            started_going = False
            '''

def onWaypointsUpdate(msg):
    global remaining_waypoints

    if len(remaining_waypoints) > 0:
        return

    string = msg.data
    split = string.split(",")
    
    nums = []
    for n in split:
        nums.append(float(n))
    
    waypoints = np.array(nums).reshape((-1, 2))
    print("Recieved new waypoints: ")
    print(waypoints)
    
    remaining_waypoints = waypoints
    create_actions()
    

def drive(forward, turning):
    twist = Twist()
    linear = Vector3()
    linear.x = forward 
    angular = Vector3()
    angular.z = turning 

    twist.linear = linear
    twist.angular = angular

    command_pub.publish(twist)

# Starting point of the code
if __name__ == "__main__":
    rospy.init_node("motion_controller")

    drive_pub = rospy.Publisher("/drive_command", Float32, queue_size=10)
    turn_pub = rospy.Publisher("/turn_command", Float32, queue_size=10);
    command_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
 
    status_pub = rospy.Publisher("/motion_handler/status", Float32, queue_size=10)
    quit_pub = rospy.Publisher("/motion_handler/quit", Float32, queue_size=10)

    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)
    rospy.Subscriber("/motion_handler/status", Float32, onStatusUpdate)
    rospy.Subscriber("/motion_handler/waypoints", String, onWaypointsUpdate)

    create_actions()
    
    rospy.spin()
