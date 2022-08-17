#!/usr/bin/env python 

from __future__ import print_function
import time

from chip_bldc_driver.msg import Command, Feedback
from std_msgs.msg import Int32
import sys

import rospy

def motor_power(i, pubs):
    if (rospy.is_shutdown()):
        sys.exit(1)


    motor_request = Command()
    command = int((i/3500.0) * 1000)
    motor_request.motor_command = command
    
    for pub in pubs:
        pub.publish(motor_request)
    
    time.sleep(0.5)
    
    print("rpm: " + str(i) + ", command: " + str(command))
    time.sleep(0.1)

if __name__ == "__main__":
    rospy.init_node("motor_stepper")
    
    motors = [2]

    pubs = []
    
    for i in motors:
        p = rospy.Publisher("/motor_driver_" + str(i) + "/Command", Command, queue_size=1)
        pubs.append(p)

    for i in range(100, 1000, 100):
        motor_power(i, pubs)
    
    #for i in range(3500, -100, -100):
    #    motor_power(i, pubs)
