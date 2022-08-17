#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
from time import time

from chip_bldc_driver.msg import Command

import rospy

if __name__ == "__main__":
    rospy.init_node("motor_rpm")

    pub = rospy.Publisher("/bldc_driver_node/Command", Command, queue_size=1)

    rpm = ((int(input("What speed? ")))/3500) * 1000
    t = float(input("How long? "))

    b = time()

    print("r")
    print(rpm)
    print("t")
    print(t)
    print("b")
    print(b)

    r = rospy.Rate(50)

    while ((time() - b <= t) and (not rospy.is_shutdown())):
        msg = Command()
        msg.motor_command = rpm
        pub.publish(msg)
        print("publishing")
        r.sleep()

    
