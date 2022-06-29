#!/usr/bin/env bash

echo "Starting camera node..." &&
	roslaunch realsense2_camera rs_camera.launch initial_reset:=true enable_gyro:=true enable_accel:=true align_depth:=true &

sleep 7s &&
       
	echo "Starting object detection node" &&
       
	rosrun ros_deep_learning detectnet /dettnet/image_in:=/camera/color/image_raw	&
       	sleep 3s &&
	       
		echo "Starting depth node" && rosrun camera detectdepth.py & sleep 2s && echo "Launch rviz to see result"

