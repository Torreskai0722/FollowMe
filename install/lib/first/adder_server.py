#!/usr/bin/env python2

from __future__ import print_function

from first.srv import AddTwoInts,AddTwoIntsResponse
import rospy


def handle_request(req):
    ans = req.a + req.b
    print("Returning " + str(req.a) + " + " + str(req.b) + " = " + str(ans))
    return AddTwoIntsResponse(ans)

def server():
    rospy.init_node('adder_server');
    s = rospy.Service('add', AddTwoInts, handle_request)
    print("Ready to add")
    rospy.spin()



if __name__ == "__main__":
    server()
