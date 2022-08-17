#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
import time

from chip_bldc_driver.msg import Command

import rospy

def motor_power(i):
    msg = Command()
    amt = i * 6
    print("now setting motor to: " + str(amt))
    msg.motor_command = amt
    pub.publish(msg)
    time.sleep(0.05)



if __name__ == "__main__":
    rospy.init_node("motor_driver")

    pub = rospy.Publisher("/bldc_driver_node/Command", Command, queue_size=1)
    
    for i in range(0, 100):
        motor_power(i)
    
    print("reached top")
    
    time.sleep(1)

    print("going down")

    for i in range(100, 0, -1):
        motor_power(i)


    
