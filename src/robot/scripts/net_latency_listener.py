#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PoseStamped, Pose, TwistStamped, Vector3
from nav_msgs.msg import Path
import sys

from std_msgs.msg import Float32
from visualization_msgs.msg import Marker, MarkerArray

# RUN THIS ON THE FOLLOWER ROBOT

deltas = []
printed = False

def onLatency(msg):
    global deltas
    global printed
    if len(deltas) == 1000:
        if not printed:
            avg = sum(deltas) / len(deltas)

            print(deltas)
            print("Average of deltas are: " + str(avg))
            print("min is " + str(min(deltas)))

            a = np.asarray(deltas)
            np.savetxt("pub_latency.csv", [a], delimiter=",")

            print("written to file")
            
            printed = True
        return
        
    delta = (msg.header.stamp - rospy.Time.now()).to_sec()
    deltas.append(delta)
    print("Delta of " + str(delta) + " added")

# Starting point of the code
if __name__ == "__main__":
    rospy.init_node("latency_subscriber")

    lsub = rospy.Subscriber("/latency/twist", TwistStamped, onLatency)

    rospy.spin()