#!/usr/bin/env python 


from __future__ import print_function
from time import time
from math import pi

import rospy

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def threshold(v, m, t):
    if (abs(v) <= t):
        return m
    return v


gyroReadings = []
gyroT0 = 0
heading = Vector3()

angleFactor = (180/pi)

def onGyro(gyro):

    global gyroReadings
    global gyroT0
    global heading

    if len(gyroReadings) < 20:
        if len(gyroReadings) == 0:
            gyroT0 = time()
        gyroReadings.append(gyro.angular_velocity)
    else:
        dt = time() - gyroT0
    
        ax = 0
        ay = 0
        az = 0
        
        for reading in gyroReadings:
             ax += threshold(reading.x * angleFactor, 0, 0.5)
             ay += threshold(reading.y * angleFactor, 0, 0.45)
             az += threshold(reading.z * angleFactor, 0, 0.4)
        
        heading.x += (ax / 20) * dt
        heading.y += (ay / 20) * dt
        heading.z += (az / 20) * dt

        print("Heading is " + str(heading))
        gyroReadings = []


if __name__ == "__main__":
    rospy.init_node("heading_tracker")

    rospy.Subscriber("/camera/gyro/sample", Imu, onGyro)

    pub = rospy.Publisher("/heading", Vector3, queue_size=1)
    
    r = rospy.Rate(30)
    while not rospy.is_shutdown():
        pub.publish(heading)
        r.sleep()

    
