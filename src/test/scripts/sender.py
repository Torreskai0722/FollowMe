#!/usr/bin/env python 

import rospy
from test.msg import SentMessage
from test.srv import *

def get_username():
    if len(sys.argv) >= 2:
        return "sender" + str(sys.argv[1])
    return "sender"

def main():
    print("b")
    username = get_username()

    print("h")

    pub = rospy.Publisher('messages', SentMessage, queue_size=10)
    print("s")

    rospy.init_node(username, anonymous=((len(sys.argv) < 2)))
    print("a")

    rospy.wait_for_service("random_number_service")
    print("s")
    get_random_number = rospy.ServiceProxy("random_number_service", RandomNumber)
    
    print("Sender Initialized")

    while not rospy.is_shutdown():
        userin = raw_input("Enter message or command: ")
        # rospy.loginfo("usrmsg: " + message_string)
        if userin == "quit":
            sys.exit(1)
        elif userin == "random":
            rand = get_random_number()
            message_string = "Random Number is: " + str(rand.random_number)
        else:
            message_string = userin

        msg = SentMessage()
        msg.sender = username
        msg.content = message_string 
        
        pub.publish(msg)

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass


