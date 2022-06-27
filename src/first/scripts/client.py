#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from first.srv import *

def client(x, y):
    rospy.wait_for_service('add')
    try:
        addS = rospy.ServiceProxy('add', AddTwoInts)
        resp1 = addS(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("call failed :%s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("answer is " + str(client(x, y)))
