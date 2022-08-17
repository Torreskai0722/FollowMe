# AMR-Dev
Development of an indoor autonomous mobile robots.


# NOTES FOR USAGE:

## Running FollowMe:

The physical implementation of FollowMe is described in our paper. In short, we have two identical differential drive bases. One of them has an NVIDIA Jetson Xavier NX, the other has a Raspberry Pi 4. The Jetson robot is the **guidance*** or **master** robot (both will be used interchangeably) and has two USB cameras (one on front and one on back) as well as a RPLidar S1 mounted on top. The Raspberry Pi Robot has no sensors and therefore has no way of localizing itself, but it does have 4 AprilTags positioned on the center of each side for the master robot's cameras to see and locate. 

### Installation:
#### Jetson Setup
1) Install Ubuntu 18.04 Bionic
2) Install ROS Melodic using [these steps](https://wiki.ros.org/melodic/Installation)
3) Clone this repo and build with `catkin-make`
    - If catkin-make failes due to missing of `Status.h` in `chip-bldc-driver`, run `catkin-make chip-bldc-driver-generate-messages` first, then rebuild the project
4) In Ubuntu settings, enable auto-login
#### Raspberry PI Setup
1) Using the Raspberry PI Imager utility, flash an SD card with **Raspberry Pi OS (Legacy)** *Buster* version. It will be near the bottom of the "other rpi os" section.
    - You can also setup SSH passwords and autologin when flashing the SD Card
2) Install ROS Melodic using [these steps](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi)
3) Clone this repo into a separate folder than the newly created `catkin-ws` from the previous step
4) Copy in ONLY the `follower_robot` and `follower_motor` directories from the cloned repo into the `catkin_ws` folder.
5) Build with `catkin-make`

#### Common Setup
1) Follow the steps in `79-robot.rules.md` to enable the correct UDEV Rules for both follower and guidance robot
    - This only needs to be done once (reboot both after doing so)
2) Run `source usbsetup.sh` on *both* machines (run this on startup or set it as a Cron job)

### Running FollowMe:
1) Run `roslaunch robot robot.launch` on the **guidance** robot and `roslaunch follower_robot robot.launch` on the **follower** robort
2) In a separate terminal on the master robot, run `rosrun robot followme.py`
3) Open RVIZ (you can use the config in `rviz/main.rviz`), specify a Nav goal, and watch the master robot navigate while the follower robot follows it. 

## If not using FollowMe:
These steps are how to run basic demos of the various sensors and motors across the robot. These are outdated if you plan on using FollowMe and the setup described in `79-robot-rules.md`.

### setup for lidar:
```sh
sudo chmod 666 /dev/ttyUSB0
roslaunch rplidar_ros rplidar_s1.launch
```

### setup for motor
```sh
sudo chmod 777 /dev/ttyUSB0
roslaunch chip_bldc_driver example.launch
```

## Demos

### Realsense Camera Demos:
Start the camera node:
`roslaunch realsense2_camera rs_camera.launch initial_reset:=true enable_gyro:=true enable_accel:=true align_depth:=true filters:=pointcloud`

Object Detection and Distance Estimation
```sh
# start the inferencing node
rosrun ros_deep_learning detectnet /dettnet/image_in:=/camera/color/image_raw
rosrun camera detectdepth.py
```

Heading Tracking with IMU:
`rosrun camera heading.py`

SLAM-type Mapping (doesn't work very well) using heading
```sh
rosrun camera mapper.py
rviz
```

### RPLidar Demos:
Start with:
```sh
roslaunch rplidar_ros rplidar_s1.launch
```

Single revolution plotted as a map:
`rosrun lidar single_map.py` 

Multi Object Detection:
```sh
rosrun lidar pointcloud.py
rosrun multi_object_tracking_lidar kf_tracker
rviz
```

### Any of the motor demos:
```sh
rosrun chip_bldc_driver bldc_driver_node
rosrun motor [stepper.py, rpm.py etc.]
```



