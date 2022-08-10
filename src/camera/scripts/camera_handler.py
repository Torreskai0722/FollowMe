#!/usr/bin/env python 


from __future__ import print_function

import rospy
import roslaunch
from std_msgs.msg import Float32

current_camera = "NONE"
lastProcess = None

def onSwitch(msg):
    global requested_camera

    requested_camera = msg.data

    if msg.data < 1.0:
        # go to front camera
        launch_camera("FRONT")
    else:
        launch_camera("BACK")

def launch_camera(camera):
    global current_camera
    global lastProcess

    if current_camera != camera and (camera == "FRONT" or camera == "BACK"):
        current_camera = camera

        # quit last camera
        if lastProcess != None:
            lastProcess.shutdown()
        
        # launch camera
        lastProcess = roslaunch.parent.ROSLaunchParent(uuid, ["/home/nvidia/projects/rosproject/src/camera/launch/" + (camera.lower()) + "cam.launch"])
        lastProcess.start()
        rospy.loginfo("switched camera to " + camera)

if __name__ == "__main__":
    rospy.init_node("camera_handler")

    rospy.Subscriber("/multicam_handler/switch", Float32, onSwitch)

    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    launch_camera("BACK")

    rospy.spin()
       

