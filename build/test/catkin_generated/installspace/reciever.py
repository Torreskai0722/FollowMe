#!/usr/bin/env python2

import rospy
from test.msg import SentMessage

def onRecieve(message):
    print(message.sender + ": " + message.content)


def main():
    rospy.init_node("reciever", anonymous=True)
    rospy.Subscriber("messages", SentMessage, onRecieve)

    rospy.spin()

if __name__ == "__main__":
    main()
