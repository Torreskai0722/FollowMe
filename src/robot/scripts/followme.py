#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PointStamped, PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path, OccupancyGrid

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32, String
from visualization_msgs.msg import Marker, MarkerArray
from actionlib_msgs.msg import GoalID

from pathsplitter import get_point_aimed

DYNAMICALLY_AJDUST_PARAMETERS = True

MIN_LOOKAHEAD = 0.25
DEFAULT_MAX_LOOKAHEAD = 0.4
PREFERRED_FOLLOWING_DISTANCE = DEFAULT_MAX_LOOKAHEAD

K_SPEED_ADJUST = 0.4
K_LOOKAHEAD_ADJUST = 0.2

REGULAR_TOLERANCE = 0.4

main_pose = Pose()
follower_pose = Pose()

global_path = []
main_has_target = False
follower_has_target = False
follower_seen = False

main_command = Twist()

main_target = Pose()
follower_target = Pose()

main_dist_from_target = 100000000
follower_dist_from_target = 1000000

CURRENT_STATE = "IDLE"
LAST_STATE = "IDLE"

IN_RECOVERY = True

def SET_STATE(state):
    global CURRENT_STATE
    global LAST_STATE

    print("Switching from " + CURRENT_STATE + " to " + state)

    LAST_STATE = CURRENT_STATE
    CURRENT_STATE = state

def idle():
    print("FollowMe Started")
    SET_STATE("SEARCH")

def search():
    print("Searching for follower")

    if (LAST_STATE != "IDLE"):
        t = Twist()
        t.angular.z = 0.125
        main_command_pub.publish(t)
        

    if follower_seen:
        # if LAST_STATE == "IDLE":
        SET_STATE("WAIT_FOR_PATH")
        main_command_pub.publish(Twist())

def wait_for_path():
    global main_has_target
    global main_target
    global follower_target

    print("Waiting for path")
    if len(global_path) > 0:
        print("Path recieved!")

        main_cancel_pub.publish(GoalID())

        # calculate main first point
        main_first_point = get_point_aimed(global_path, main_pose, follower_pose, DEFAULT_MAX_LOOKAHEAD, MIN_LOOKAHEAD)
        print(main_first_point)

        if main_first_point != None:

            # for rviz display
            p = PointStamped()
            p.header.stamp = rospy.Time.now()
            p.header.frame_id = "map"
            p.point.x = main_first_point.position.x
            p.point.y = main_first_point.position.y
            point_pub.publish(p)

            main_target = main_first_point
            main_has_target = True

            follower_target = main_pose

            ps = PoseStamped()
            ps.header.frame_id = "map"
            ps.header.stamp = rospy.Time.now()
            ps.pose = main_first_point

            main_target_pub.publish(ps)

            SET_STATE("MAIN_TO_FIRST")
        else:
            # something bad happened
            SET_STATE("END")

def main_to_first():
    global main_has_target
    global follower_has_target

    print("Driving to first target" + str(main_dist_from_target))
    if abs(main_dist_from_target) < REGULAR_TOLERANCE:
        main_has_target = False
        follower_has_target = True 

        SET_STATE("FOLLOWER_TO_OG")

follower_iters = 0
def follower_to_og():
    global follower_has_target
    global follower_iters
    global main_target
    global global_path

    if not follower_seen and follower_iters < 25:
        SET_STATE("SEARCH")
    
    if IN_RECOVERY:
        main_target = global_path[len(global_path) - 1]

        ps = PoseStamped()
        ps.header.frame_id = "map"
        ps.header.stamp = rospy.Time.now()
        ps.pose = main_target

        main_target_pub.publish(ps)

        SET_STATE("RECOVERY_LOOP")
        return

    follower_iters += 1
    main_cancel_pub.publish(GoalID())
    
    if abs(follower_dist_from_target) < (REGULAR_TOLERANCE/2):
        follower_cancel_pub.publish(GoalID())
        follower_has_target = False
        SET_STATE("GO_DRIVE")
    else:
        ps = PoseStamped()
        ps.header.frame_id = "map"
        ps.header.stamp = rospy.Time.now()
        ps.pose = follower_target

        print(follower_target)
        
        follower_target_pub.publish(ps)

        print("follower going: " + str(follower_dist_from_target))


def distance_between_poses(a_pose, b_pose):
    a = a_pose.position
    b = b_pose.position
    return math.hypot(a.x - b.x, a.y - b.x)


entered_go_drive = True
average_distance = 0
n_samples = 0

main_speed = 0

def go_drive():
    global entered_go_drive
    global average_distance
    global n_samples
    global follower_target
    global main_target
    global main_dist_from_target
    global global_path
    global main_pose
    global follower_pose

    if entered_go_drive:
        
        main_max_dist = rospy.get_param("/followme/max_lookahead", DEFAULT_MAX_LOOKAHEAD)

        next_point = get_point_aimed(global_path, main_pose, follower_pose, main_max_dist, MIN_LOOKAHEAD) 
        ps = PoseStamped()
        ps.header.frame_id = "map"
        ps.header.stamp = rospy.Time.now()
        ps.pose = next_point

        main_target = next_point
        main_target_pub.publish(ps)

        follower_target = main_pose

        ps = PoseStamped()
        ps.header.frame_id = "map"
        ps.header.stamp = rospy.Time.now()
        ps.pose = follower_target

        follower_target_pub.publish(ps)
        
        entered_go_drive = False

    if main_dist_from_target < REGULAR_TOLERANCE:
        follower_cancel_pub.publish(GoalID())
        main_cancel_pub.publish(GoalID())

        if distance_between_poses(global_path[len(global_path - 1)], main_pose) < REGULAR_TOLERANCE:
            SET_STATE("END")
        else:
            SET_STATE("ASSESS")

    average_distance = ((average_distance * n_samples) + distance_between_poses(main_pose, follower_pose))/(n_samples + 1)
    n_samples += 1
    

def assess():
    global entered_go_drive
    entered_go_drive = True

    main_speed = rospy.get_param("/move_base/DWAPlannerROS/max_vel_x")
    max_lookahead = rospy.get_param("/followme/max_lookahead", DEFAULT_MAX_LOOKAHEAD) 

    delta_from_avg = average_distance - PREFERRED_FOLLOWING_DISTANCE
    pct_error = delta_from_avg / PREFERRED_FOLLOWING_DISTANCE

    speed_adjustment_factor = pct_error * K_SPEED_ADJUST
    lookahead_adjustment_factor = -pct_error * K_LOOKAHEAD_ADJUST

    if DYNAMICALLY_AJDUST_PARAMETERS:
        rospy.set_param("/move_base/DWAPlannerROS/max_vel_x", main_speed + speed_adjustment_factor)
        rospy.set_param("/followme/max_lookahead", max_lookahead + lookahead_adjustment_factor)
        
        if abs(pct_error) < 0.3:
            SET_STATE("GO_DRIVE")
        else:
            SET_STATE("RECOVERY")

def recovery():
    global IN_RECOVERY

    print("ENTERED RECOVERY STATE")
    IN_RECOVERY = True
    SET_STATE("SEARCH")

def recovery_loop():
    global main_target
    global main_dist_from_target
    global main_pose
    global global_path

    if distance_between_poses(main_pose, global_path[len(global_path) - 1]) > 0.4:
        follower_command_pub.publish(main_command)
    else:
        follower_command_pub.publish(Twist())
        main_cancel_pub.publish(GoalID())
        SET_STATE("END")

def end():
    follower_command_pub.publish(Twist())
    main_command_pub.publish(Twist())
    main_cancel_pub.publish(GoalID())
    follower_cancel_pub.publish(GoalID())
    pass

STATES = {
    "IDLE": idle,
    "SEARCH": search,
    "WAIT_FOR_PATH": wait_for_path,
    "MAIN_TO_FIRST": main_to_first,
    "FOLLOWER_TO_OG": follower_to_og,
    "GO_DRIVE": go_drive,
    "ASSESS": assess,
    "RECOVERY": recovery,
    "RECOVERY_LOOP": recovery_loop,
    "END": end,
}

def onMainOdometryUpdate(msg):
    global main_pose
    global main_dist_from_target

    main_pose = msg.pose

    if main_has_target:
        main_dist_from_target = math.hypot(main_pose.position.x - main_target.position.x, main_pose.position.y - main_target.position.y)

def onFollowerOdometryUpdate(msg):
    global follower_pose
    global follower_dist_from_target

    follower_pose = msg.pose

    if follower_has_target:
        follower_dist_from_target =  math.hypot(follower_pose.position.x - follower_target.position.x, follower_pose.position.y - follower_target.position.y)

def onMainCommandRecieved(msg):
    global main_command
    main_command = msg

def onPathUpdate(msg):
    global global_path
    if len(global_path) == 0:
        for ps in msg.poses:
            global_path.append(ps.pose)

def onLocalizerStatusUpdate(msg):
    global follower_seen
    follower_seen = True if msg.data == 1.0 else False

if __name__ == "__main__":
    rospy.init_node("FollowMeCoordinator")

    rospy.Subscriber("/follower/follower_pose", PoseStamped, onFollowerOdometryUpdate)
    rospy.Subscriber("/move_base/NavfnROS/plan", Path, onPathUpdate)
    rospy.Subscriber("/slam_out_pose", PoseStamped, onMainOdometryUpdate)
    rospy.Subscriber("/cmd_vel", Twist, onMainCommandRecieved)
    rospy.Subscriber("/follower/localizer_status", Float32, onLocalizerStatusUpdate)
    
    cur_state_pub = rospy.Publisher("/follow_me_state", String, queue_size=10)
    main_target_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
    follower_target_pub = rospy.Publisher("/follower_nav/move_base_simple/goal", PoseStamped, queue_size=10)
    point_pub = rospy.Publisher("/clicked_point", PointStamped, queue_size=10)

    main_command_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    follower_command_pub = rospy.Publisher("/follower_nav/cmd_vel", Twist, queue_size=10)
    main_cancel_pub = rospy.Publisher("/move_base/cancel", GoalID, queue_size=10)
    follower_cancel_pub = rospy.Publisher("/follower_nav/follower_move_base/cancel", GoalID, queue_size=10)

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        print("Current state is: " + CURRENT_STATE)
        cur_state_pub.publish(CURRENT_STATE)

        STATES[CURRENT_STATE]()

        rate.sleep()