#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PointStamped, PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path, OccupancyGrid

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32, String
from visualization_msgs.msg import Marker, MarkerArray

target_pose = Pose()
midpoint = []
mypose = []
quat = None
def onPointClicked(msg):
    global target_pose
    global midpoint

    if len(mypose) == 0:
        return

    target_pose.position.x = msg.point.x
    target_pose.position.y = msg.point.y
    target_pose.orientation = quat

    midpoint = [
        (msg.point.x + mypose[0])/5,
        (msg.point.y + mypose[1])/5
    ]

    ps = PoseStamped()

    ps.header = msg.header

    ps.pose.position.x = midpoint[0]
    ps.pose.position.y = midpoint[1]
    ps.pose.orientation = quat

    print("Got target, routing to midpoint now")
    target_pub.publish(ps)

def onOdometryUpdate(msg):
    global mypose
    global quat
    pose = msg.pose.position
    mypose = [pose.x, pose.y]
    quat = msg.pose.orientation
    if len(midpoint) > 0:
        if math.hypot(midpoint[0] - pose.x, midpoint[1] - pose.y) < 0.1:
            print("Reached midpoint")
            ps = PoseStamped()
            ps.header.stamp = msg.header.stamp
            ps.header.frame = "map"
            ps.pose = target_pose
            target_pub.publish(ps)

if __name__ == "__main__":
    rospy.init_node("less_naive")

    rospy.Subscriber("/clicked_point", PointStamped, onPointClicked)
    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)
    
    target_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)

    rospy.spin()
