# FollowMe:
FollowMe is a system designed at the C.A.R Lab at Wayne State University that allows for one robot with sensors to guide another robot without sensors through a path. The system and our implementation are described in our [paper](#). The framework is comprised of a state machine and an adaptive path segmentation algorithm that can be used in a variety of applications and situations. This repository contains a ROS implementation of the FollowMe system and was tested on differential drive robots in real life and in a simulation. Below is a series of steps to get FollowMe running on a similar system with two robots.

### Our Implementation
The full implementation is more thoroughly explained in the [paper](#). In short, we have two identical front differential drive bases. One of them has an NVIDIA Jetson Xavier NX, the other has a Raspberry Pi 4. The Jetson robot is the **guidance*** or **master** robot (both terms will be used interchangeably) and has two USB cameras (one on front and one on back) as well as a RPLidar S1 mounted on top. The Raspberry Pi Robot has no sensors and therefore has no way of localizing itself, but it does have 4 AprilTags positioned on the center of each side for the master robot's cameras to see and locate. 

## Installation:
### Jetson Setup
1) Install Ubuntu 18.04 Bionic
2) Install ROS Melodic using [these steps](https://wiki.ros.org/melodic/Installation)
3) Clone this repo and build with `catkin-make`
    - If catkin-make failes due to missing of `Status.h` in `chip-bldc-driver`, run `catkin-make chip-bldc-driver-generate-messages` first, then rebuild the project
4) In Ubuntu settings, enable auto-login

### Raspberry PI Setup
1) Using the Raspberry PI Imager utility, flash an SD card with **Raspberry Pi OS (Legacy)** *Buster* version. It will be near the bottom of the "other rpi os" section.
    - You can also setup SSH passwords and autologin when flashing the SD Card
2) Install ROS Melodic using [these steps](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi)
3) Clone this repo into a separate folder than the newly created `catkin-ws` from the previous step
4) Copy in ONLY the `follower_robot` and `follower_motor` directories from the cloned repo into the `catkin_ws` folder.
5) Build with `catkin-make`

### Common Setup
1) Follow the steps in `79-robot.rules.md` to enable the correct UDEV Rules for both follower and guidance robot
    - This only needs to be done once (reboot both after doing so)
2) Run `source usbsetup.sh` on *both* machines (run this every time on startup or set it as a Cron job)

**SSH Setup:**
It is recommended to not have either the Jetson or Raspberry Pi connected via HDMI while it is moving (for obvious reasons). You can use a separate computer (any OS) or a Linux one with ROS installed (melodic or noetic) to use RVIZ and other utilities. 

1) Get the IP Address of each machine and note it down by running `ifconfig` and checking the `inet` entry under `wlan0`. Ensure that each robot's computer is set to autologin, and you can disconnect and you should not have to connect again.
2) Using the central computer (neither of the robots), edit `/etc/hosts` (or your OS's equivalent) to give a name to each computer (I used `jetson` and `raspberrypi`)
3) Run `ssh [username]@[computer_name]` for each robot in a new terminal window (ex: `ssh nvidia@jetson`)
4) Set the environment variable of `$ROS_IP` on **ALL MACHINES** (including remote computer) to their respective IPs
5) On all machines except the Master/Guidance robot, add the master robot to the list in `/etc/hosts`
6) On all machines except the Master/Guidance robot, set the environment variable of `$ROS_MASTER_URI` to `http://[computer_name]:11311` (ex: `http://jetson:11311`)
    - You should put the commands for steps 4 and 6 in the `.bashrc` or your shell's run configuration file to run every time a shell is opened. 

## Running FollowMe:
1) Complete all installation and common setup steps above.
2) Run `roslaunch robot robot.launch` on the **guidance** robot and `roslaunch follower_robot robot.launch` on the **follower** robort
3) In a separate terminal on the master robot, run `rosrun robot followme.py`
4) Open RVIZ on the remote computer (you can use the config included in `rviz/main.rviz`), specify a Nav goal, and watch the master robot navigate while the follower robot follows it. 

<hr>

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

### Demos

#### Realsense Camera Demos:
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

#### RPLidar Demos:
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

#### Any of the motor demos:
```sh
rosrun chip_bldc_driver bldc_driver_node
rosrun motor [stepper.py, rpm.py etc.]
```



