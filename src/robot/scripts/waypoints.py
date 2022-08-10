#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PointStamped, PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path, OccupancyGrid

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32, String
from visualization_msgs.msg import Marker, MarkerArray

def onPointClicked(msg):
    point = msg.point
    waypoint_arr = np.array([[point.x, point.y]]).flatten()
    
    waypoint_str = ""
    for waypoint in waypoint_arr:
        waypoint_str += str(waypoint) + ","
    waypoint_str = waypoint_str[:-1]

    print("publishing waypoints " + waypoint_str)

    waypoint_pub.publish(waypoint_str)
    
if __name__ == "__main__":
    rospy.init_node("waypoint_tracker")

    rospy.Subscriber("/clicked_point", PointStamped, onPointClicked)
    waypoint_pub = rospy.Publisher("/motion_handler/waypoints", String, queue_size=10)

    rospy.spin()
