#!/usr/bin/env python

from __future__ import print_function

from test.srv import RandomNumber, RandomNumberResponse 
import rospy
import random

def handle(req):
    num = random.randint(1, 1000)
    print("recieved a request for a random number: " + str(num))
    return RandomNumberResponse(num)

if __name__ == "__main__":
    print("Random number service started")
    rospy.init_node("random_server")
    s = rospy.Service("random_number_service", RandomNumber, handle)
    rospy.spin()


