#!/usr/bin/env python2

import numpy as np
import time
import math

import rospy
from geometry_msgs.msg import PoseStamped, Pose, Twist, Vector3
from std_msgs.msg import Float32

from tf.transformations import euler_from_quaternion, quaternion_from_euler

# Parameters
k = 1.0  # look forward gain
Lfc = 0.1  # [m] look-ahead distance
dt = 0.1
Kp = 1.0  # speed proportional gain
WB = 0.49  # [m] wheel base of vehicle


class State:

    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.rear_x = self.x - ((WB / 2) * math.cos(self.yaw))
        self.rear_y = self.y - ((WB / 2) * math.sin(self.yaw))

    def update(self, a, delta):
        self.x += self.v * math.cos(self.yaw) * dt
        self.y += self.v * math.sin(self.yaw) * dt
        self.yaw += self.v / WB * math.tan(delta) * dt
        self.v += a * dt
        self.rear_x = self.x - ((WB / 2) * math.cos(self.yaw))
        self.rear_y = self.y - ((WB / 2) * math.sin(self.yaw))

    def calc_distance(self, point_x, point_y):
        dx = self.rear_x - point_x
        dy = self.rear_y - point_y
        return math.hypot(dx, dy)


class States:

    def __init__(self):
        self.x = []
        self.y = []
        self.yaw = []
        self.v = []
        self.t = []

    def append(self, t, state):
        self.x.append(state.x)
        self.y.append(state.y)
        self.yaw.append(state.yaw)
        self.v.append(state.v)
        self.t.append(t)


def proportional_control(target, current):
    a = Kp * (target - current)

    return a


class TargetCourse:

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.old_nearest_point_index = None

    def search_target_index(self, state):

        # To speed up nearest point search, doing it at only first time.
        if self.old_nearest_point_index is None:
            # search nearest point index
            dx = [state.rear_x - icx for icx in self.cx]
            dy = [state.rear_y - icy for icy in self.cy]
            d = np.hypot(dx, dy)
            ind = np.argmin(d)
            self.old_nearest_point_index = ind
        else:
            ind = self.old_nearest_point_index
            distance_this_index = state.calc_distance(self.cx[ind],
                                                      self.cy[ind])
            while True:
                distance_next_index = state.calc_distance(self.cx[ind + 1],
                                                          self.cy[ind + 1])
                if distance_this_index < distance_next_index:
                    break
                ind = ind + 1 if (ind + 1) < len(self.cx) else ind
                distance_this_index = distance_next_index
            self.old_nearest_point_index = ind

        Lf = k * state.v + Lfc  # update look ahead distance

        # search look ahead target point index
        while Lf > state.calc_distance(self.cx[ind], self.cy[ind]):
            if (ind + 1) >= len(self.cx):
                break  # not exceed goal
            ind += 1

        return ind, Lf


def pure_pursuit_steer_control(state, trajectory, pind):
    ind, Lf = trajectory.search_target_index(state)

    if pind >= ind:
        ind = pind

    if ind < len(trajectory.cx):
        tx = trajectory.cx[ind]
        ty = trajectory.cy[ind]
    else:  # toward goal
        tx = trajectory.cx[-1]
        ty = trajectory.cy[-1]
        ind = len(trajectory.cx) - 1

    alpha = math.atan2(ty - state.rear_y, tx - state.rear_x) - state.yaw

    delta = math.atan2(2.0 * WB * math.sin(alpha) / Lf, 1.0)

    return delta, ind

leftSpeed = 0
rightSpeed = 0

def onLeftSpeedUpdate(speed):
    global leftSpeed
    leftSpeed = speed.data

def onRightSpeedUpdate(speed):
    global rightSpeed
    rightSpeed = speed.data

target_speed = 0.5 # [m/s]

lastOdometry = PoseStamped()
curPose = Pose()
lastTime = 0
reached_goal = False
started = False

def onOdometryUpdate(odometry):
    global lastSlam
    global curPose
    global reached_goal
    global target_ind
    global target_course
    global dt
    global lastTime
    global started

    curPose = odometry.pose

    if not started:
        state = State(x=curPose.position.x, y=curPose.position.y, yaw=0.0, v=0.0)
        time_current = time.time()
        states = States()
        states.append(time, state)
        target_course = TargetCourse(cx, cy)
        target_ind, _ = target_course.search_target_index(state)
        started = True
        return

    if lastTime == 0:
        lastTime = time.time()
        dt = 0.1
    else:
        dt = time.time() - lastTime

    if lastIndex <= target_ind:
        print('reached goal')
        print(target_ind)
        reached_goal = True

    if (reached_goal):
        twist = Twist()
        command_pub.publish(twist)
        return


    velocity = 0
    if lastTime != 0:
        velocity = (leftSpeed + rightSpeed)/2

    ai = proportional_control(target_speed, velocity)

    curState = State(x = curPose.position.x, y = curPose.position.y, yaw = 0, v=velocity)
    di, target_ind = pure_pursuit_steer_control(curState, target_course, target_ind)

    print("Current target ind is " + str(target_ind) + " out of " + str(lastIndex))
    print("Cur pos is " + str(curState.x) + ", " + str(curState.y))
    print("slam out pose " + str(curPose.position.x) + ", " + str(curPose.position.y))
    

    print("Calculated linear " + str(ai) + ", angular " + str(di))

    twist = Twist()
    linear = Vector3()
    linear.x = ai
    angular = Vector3()
    angular.z = di

    twist.linear = linear
    twist.angular = angular
    # command_pub.publish(twist)

    lastOdometry = odometry
    lastTime = time.time()


if __name__ == "__main__":
    cx = []
    cy = []
    for i in range(0, 2, 1):
        cx.append(float(i)/10)
        cy.append(0)
    
    rospy.init_node("pure_pursuit")

    print(cx)
    print(cy)

    lastIndex = len(cx) - 1

    command_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("/slam_out_pose", PoseStamped, onOdometryUpdate)

    rospy.Subscriber("/drivebase_speeds/left", Float32, onLeftSpeedUpdate)
    rospy.Subscriber("/drivebase_speeds/right", Float32, onRightSpeedUpdate)

    rospy.spin()
