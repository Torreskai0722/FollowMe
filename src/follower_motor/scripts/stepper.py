#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
import time
import sys

from chip_bldc_driver.msg import Command, Feedback
from std_msgs.msg import Int32

import rospy

def motor_power(i, pub, target_pub):
    if (rospy.is_shutdown()):
        sys.exit(1)
    motor_request = Command()
    command = int((i/3500.0) * 1000)
    motor_request.motor_command = command
    
    pub.publish(motor_request)
    target_pub.publish(i)
    
    time.sleep(0.5)
    
    print("rpm: " + str(i) + ", command: " + str(command))
    time.sleep(0.1)

if __name__ == "__main__":
    rospy.init_node("motor_stepper")

    pub = rospy.Publisher("/bldc_driver_node/Command", Command, queue_size=1)
    target_pub = rospy.Publisher("target_rpm", Int32, queue_size=1)

    for i in range(100, 3600, 100):
        motor_power(i, pub, target_pub)

    for i in range(3500, -100, -100):
        motor_power(i, pub, target_pub)
