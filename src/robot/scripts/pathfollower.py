#!/usr/bin/env python2

import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path

from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float32
from visualization_msgs.msg import Marker, MarkerArray


class State():
    def __init__(self, x_, y_, theta_):
        if not (x_ is None or y_ is None or theta_ is None):
            self.x = x_
            self.y = y_
            self.theta = theta_
        else:
            self.x = 0
            self.y = 0
            self.theta = 0

    def __str__(self):
        return str(self.x)+","+str(self.y)+","+str(self.theta)


class Controller():
    def __init__(
            self, start_, goal_, R_=0.49, L_=0.1,
            kP=0.8, kI=0.0, kD=0.01, dT=0.1, v=1.0,
            arrive_distance=0.5):

        self.current = start_
        self.goal = goal_
        self.R = R_  # in meter
        self.L = L_  # in meter

        self.E = 0   # Cummulative error
        self.old_e = 0  # Previous error

        self.Kp = kP
        self.Ki = kI
        self.Kd = kD

        self.desiredV = v
        self.dt = dT  # in second
        self.arrive_distance = arrive_distance
        return

    def uniToDiff(self, v, w):
        vR = (2*v + w*self.L)/(2*self.R)
        vL = (2*v - w*self.L)/(2*self.R)
        return vR, vL

    def diffToUni(self, vR, vL):
        v = self.R/2*(vR+vL)
        w = self.R/self.L*(vR-vL)
        return v, w

    def iteratePID(self):
        # Difference in x and y
        d_x = self.goal.x - self.current.x
        d_y = self.goal.y - self.current.y

        # Angle from robot to goal
        g_theta = np.arctan2(d_y, d_x)

        # Error between the goal angle and robot angle
        alpha = g_theta - self.current.theta
        # alpha = g_theta - math.radians(90)
        e = np.arctan2(np.sin(alpha), np.cos(alpha))

        e_P = e
        e_I = self.E + e
        e_D = e - self.old_e

        # This PID controller only calculates the angular
        # velocity with constant speed of v
        # The value of v can be specified by giving in parameter or
        # using the pre-defined value defined above.
        w = self.Kp*e_P + self.Ki*e_I + self.Kd*e_D

        w = np.arctan2(np.sin(w), np.cos(w))

        self.E = self.E + e
        self.old_e = e
        v = self.desiredV

        return v, w

    def fixAngle(self, angle):
        return np.arctan2(np.sin(angle), np.cos(angle))

    def makeAction(self, v, w):
        x_dt = v*np.cos(self.current.theta)
        y_dt = v*np.sin(self.current.theta)
        theta_dt = w

        self.current.x = self.current.x + x_dt * self.dt
        self.current.y = self.current.y + y_dt * self.dt
        self.current.theta = self.fixAngle(
            self.current.theta + self.fixAngle(theta_dt * self.dt))
        return

    def isArrived(self):
        # print("Arrive check:", str(abs(self.current.x - self.goal.x)),
        #       str(abs(self.current.y - self.goal.y)))
        current_state = np.array([self.current.x, self.current.y])
        goal_state = np.array([self.goal.x, self.goal.y])
        difference = current_state - goal_state

        distance_err = np.dot(difference, difference.T)
        if distance_err < self.arrive_distance:
            return True
        else:
            return False

    def runPID(self, odometry_state):
        if (not self.isArrived()):
            self.current.x = odometry_state.position.x
            self.current.y = odometry_state.position.y
            pose = odometry_state
            _, _, yaw = euler_from_quaternion((pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w))

            self.current.theta = yaw
            
            v, w = self.iteratePID()

            twist = Twist()
            linear = Vector3()
            linear.x = v
            angular = Vector3()
            angular.z = w

            twist.linear = linear
            twist.angular = angular

            command_pub.publish(twist)

            # self.makeAction(v, w)
            # x.append(self.current.x)
            # y.append(self.current.y)
            # theta.append(self.current.theta)
            # time.sleep(self.dt)

            # Print or plot some things in here
            # Also it can be needed to add some max iteration for
            # error situations and make the code stable.
            # print(self.current.x, self.current.y, self.current.theta)
        return self.isArrived()

current = None
cur_idx = 0

def trackRoute(start, odometry_state):
    global current_target
    global cur_idx
    global targets
    global current

    if not current:
        current = start

    if current_target == None:
        print("Done following")
        twist = Twist()
        command_pub.publish(twist)
        return

    controller = Controller(current, current_target)

    reached = controller.runPID(odometry_state)
    current = controller.current

    if reached:
        print("on to next target")

        cur_idx += 1
        if cur_idx < len(targets):
            current_target = targets[cur_idx]
        else:
            current_target = None

current_target = None
targets = []

def onOdometryUpdate(odometry):
    global begun_tracking
    global current_target
    global targets
    global start

    curpose = odometry.pose
    pose = curpose
    _, _, yaw = euler_from_quaternion((pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w))

    if not begun_tracking:
        start = State(curpose.position.x, curpose.position.y, 0.0)
        targets = [
            State(1, 0.0, 0),
            State(2, 1.0, math.pi )
        ]

        waypoints = [start]
        for t in targets:
            waypoints.append(t)

        drawnPath = Path()
        drawnPath.header.stamp = rospy.Time.now()
        drawnPath.header.frame_id = "/map"

        poses = []
        markerArray = MarkerArray()
        m_id = 0
        for t_arget in waypoints:
            ps = PoseStamped()
            ps.header = drawnPath.header
            ps.pose.position.x = t_arget.x
            ps.pose.position.y = t_arget.y
            ps.pose.position.z = 0

            x, y, z, w = quaternion_from_euler(0, 0, t_arget.theta)

            ps.pose.orientation.x = x
            ps.pose.orientation.y = y
            ps.pose.orientation.z = z
            ps.pose.orientation.w = w
            poses.append(ps)

            marker = Marker()
            marker.header.frame_id = "/map"
            marker.header.stamp = rospy.Time.now()
            marker.type = marker.SPHERE
            marker.action = marker.ADD
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.id = m_id

            m_id += 1

            marker.pose = ps.pose
            markerArray.markers.append(marker)

        marker_pub.publish(markerArray)
        
        drawnPath.poses = poses
        path_pub.publish(drawnPath)

        current_target = targets[0]
        cur_idx = 0
        begun_tracking = True
        return


    trackRoute(start, curpose)

leftSpeed = 0
rightSpeed = 0

def onLeftSpeedUpdate(speed):
    global leftSpeed
    leftSpeed = speed

def onRightSpeedUpdate(speed):
    global rightSpeed
    rightSpeed = speed

def initialize_values():
    global begun_tracking


# Starting point of the code
if __name__ == "__main__":
    # Define dt time, create controller, define start and goal points
    # In every iteration, get an action from PID and make the action,
    # after that, sleep for dt. Repeat that loop until reaching the goal state.

    rospy.init_node("pure_pursuit")

    begun_tracking = False

    command_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    path_pub = rospy.Publisher("/pathtracker_path", Path, queue_size=5)
    marker_pub = rospy.Publisher("/waypoints", MarkerArray, queue_size=10)
    
    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)
    rospy.Subscriber("/drivebase_speeds/left", Float32, onLeftSpeedUpdate)
    rospy.Subscriber("/drivebase_speeds/right", Float32, onRightSpeedUpdate)

    rospy.spin()
