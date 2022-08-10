#!/usr/bin/env python2 
import rospy

from geometry_msgs.msg import PointStamped, Pose

from std_msgs.msg import Float32

waypoints = []
args = []

COMMANDS = {}
NEEDED_ARGS = {
    "set_camera": "'front' or 'back' for which camera to use"
}

def help():
    helpstr = "CONSOLE: The available commands are: "
    for command in COMMANDS.keys():
        helpstr += command + ( ("-arguments: (" + NEEDED_ARGS[command] + ")") if command in NEEDED_ARGS.keys() else "") + ", "
    
    print(helpstr[:-2])

def clear():
    waypoints = []
    print("CONSOLE: Waypoints have been cleared")

def printWaypoints():
    waypointsStr = "CONSOLE: "
    for waypoint in waypoints:
        waypointsStr += "(" + str(waypoint.x) + ", " + str(waypoint.y) + "), "
    
    print(waypointsStr[:-2])

def drive():
    if len(waypoints > 0):
        print("CONSOLE: Starting to follow path now")
    else:
        print("ERROR: No waypoints specified")

def set_camera():
    if len(args) > 0:
        cam = args[0]
        if cam.strip().lower() == "front":
            camera_switch_pub.publish(0.0)
        else:
            camera_switch_pub.publish(1.0)
        print("CONSOLE: Camera Switched")
    else:
        print("ERROR: No camera specified")

def driveAndFollow():
    drive()

COMMANDS = {
    "help": help,
    "clear": clear,
    "waypoints": printWaypoints,
    "run": drive,
    "set_camera": set_camera,
    "run+follow": driveAndFollow
}

def onPointClicked(point):
    waypoints.append(point.point)
    print("RVIZ: Waypoint added")

if __name__ == "__main__":
    rospy.init_node("testing_console")

    rospy.Subscriber("/clicked_point", PointStamped, onPointClicked)
    camera_switch_pub = rospy.Publisher("/multicam_handler/switch", Float32, queue_size=10)
    while not rospy.is_shutdown():
        command = input("-: ")
        print(type(cmd))
        if command == "quit":
            exit(0)
        # args = cmd.split(" ")[1:]
        # if cmd in COMMANDS.keys():
        # cmd()
        # else:
        #     print("ERROR: Command '" + cmd + "' not found")


