#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path, OccupancyGrid

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32, String
from visualization_msgs.msg import Marker, MarkerArray

cur_pose = [0.0, 0.0]

def onOccupancyGrid(map):
    resolution = map.info.resolution
    width = map.info.width
    height = map.info.height
    origin = map.info.origin

    data = map.data

    grid = np.array(data).reshape((width, height))

    robot_coords = [cur_pose[0] - origin.position.x, cur_pose[1] - origin.position.y]
    robot_coords = [int(robot_coords[0] / resolution), int(robot_coords[0] / resolution)]

    # print(grid[robot_coords[0]][robot_coords[1]])

    search_radius = 4
    points = []

    for x in range(robot_coords[0] - int(search_radius / resolution), robot_coords[0] + int(search_radius / resolution)):
        for y in range(robot_coords[1] - int(search_radius / resolution), robot_coords[1] + int(search_radius / resolution)):
            if grid[x][y] == -1:
                points.append([x, y])
    
    best_candidate = [[], 100000000000000]
    for p in points:
        dx = cur_pose[0] - (p[0] / resolution)
        dy = cur_pose[1] - (p[1] / resolution)
        dt = math.atan2(dx, dy)
        
        weight = math.hypot(dx, dy)
        smaller = weight < best_candidate[1]

        if smaller:
            best_candidate[0] = [(p[0] * resolution) + origin.position.x , (p[1] * resolution) + origin.position.y]
            best_candidate[1] = weight

    print(best_candidate[0])

def onOdometryUpdate(msg):
    global cur_pose

    p = msg.pose.position
    cur_pose = [p.x, p.y]

if __name__ == "__main__":
    rospy.init_node("explorer")

    rospy.Subscriber("/map", OccupancyGrid, onOccupancyGrid)
    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)

    rospy.spin()
