#!/usr/bin/env python2 
import numpy as np
import math
import rospy

from geometry_msgs.msg import PointStamped, PoseStamped, Pose, Twist, Vector3
from nav_msgs.msg import Path, OccupancyGrid

from tf.transformations import euler_from_quaternion, quaternion_from_euler
import tf
from std_msgs.msg import Float32, String

from apriltag_ros.msg import AprilTagDetection, AprilTagDetectionArray

TAG_IDS = [0, 1, 2, 3]

TAG_TO_FOLLOWER_ROTATION_OFFSETS = [
    # zR, yR, xR all in radians
    [1.5707963268, -1.5707963268, 0.0],
    [0.0, 0.0, -1.5707963268],
    [-1.5707963268, 1.5707963268, 0.0],
    [0.0, 3.1415926, -1.5707963268]
]

TAG_TO_FOLLOWER_TRANSLATION_OFFSETS = [
    # x, y, z all in meters
    [0.0, -0.155, -0.2],
    [0.03, -0.1225, -0.1825],
    [0.0, -0.115, -0.253],
    [0.0, -0.13, -0.19]
]

def onDetectionsUpdate(detections):
    sees = (len(detections.detections) > 0)

    if sees:
        tag_id = detections.detections[0].id[0]
        sees = tag_id in TAG_IDS

    sees_pub.publish(1.0 if sees else 0.0)

    if sees:
        translation = TAG_TO_FOLLOWER_TRANSLATION_OFFSETS[tag_id]
        rotation = TAG_TO_FOLLOWER_ROTATION_OFFSETS[tag_id]

        quat = quaternion_from_euler(rotation[2], rotation[1], rotation[0] + (3.1415926 if (tag_id == 0 or tag_id == 2) else -3.1415936))
        br = tf.TransformBroadcaster()
        br.sendTransform(
            (translation[0], translation[1], translation[2]),
            quat,
            detections.header.stamp - rospy.Duration.from_sec(0.3),
            "/follower_footprint",
            "/tag_" + str(tag_id)
        )

        try:
            (trans,rot) = listener.lookupTransform('/map', '/follower_footprint', rospy.Time(0))
            
            msg = PoseStamped()

            msg.header.frame_id = "map"
            msg.header.stamp = rospy.Time.now()

            msg.pose.position.x = trans[0]
            msg.pose.position.y = trans[1]
            msg.pose.position.z = trans[2]
            msg.pose.orientation.x = rot[0]
            msg.pose.orientation.y = rot[1]
            msg.pose.orientation.z = rot[2]
            msg.pose.orientation.w = rot[3]

            pose_pub.publish(msg)

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            pass
        
    
if __name__ == "__main__":
    rospy.init_node("follower_localizer")

    rospy.Subscriber("/tag_detections", AprilTagDetectionArray, onDetectionsUpdate)
    listener = tf.TransformListener()

    sees_pub = rospy.Publisher("/follower/localizer_status", Float32, queue_size=10)
    pose_pub = rospy.Publisher("/follower/follower_pose", PoseStamped, queue_size=10)

    rospy.spin()
