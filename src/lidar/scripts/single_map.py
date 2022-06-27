#!/usr/bin/env python 

from __future__ import print_function
from matplotlib import pyplot as plt
import math
import numpy as np

from sensor_msgs.msg import LaserScan
import rospy

def onRecieve(data):
    angleMin = data.angle_min
    increment = data.angle_increment
    curAngle = angleMin

    xValues = [0]
    yValues = [0]
    
    for dist in data.ranges:
        x = dist * math.cos(curAngle)
        y = dist * math.sin(curAngle)

        xValues.append(x)
        yValues.append(y)

        curAngle += increment
    
    plt.scatter(np.array(xValues), np.array(yValues))
    plt.show()

    sys.exit(0)

if __name__ == "__main__":
    rospy.init_node("singlegraph")
    rospy.Subscriber("scan", LaserScan, onRecieve)
    rospy.spin()
