# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nvidia/projects/rosproject/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nvidia/projects/rosproject/build

# Utility rule file for _run_tests_robot_roslaunch-check_launch.

# Include the progress variables for this target.
include robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/progress.make

robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch:
	cd /home/nvidia/projects/rosproject/build/robot && ../catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/catkin/cmake/test/run_tests.py /home/nvidia/projects/rosproject/build/test_results/robot/roslaunch-check_launch.xml "/usr/bin/cmake -E make_directory /home/nvidia/projects/rosproject/build/test_results/robot" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/nvidia/projects/rosproject/build/test_results/robot/roslaunch-check_launch.xml\" \"/home/nvidia/projects/rosproject/src/robot/launch\" "

_run_tests_robot_roslaunch-check_launch: robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch
_run_tests_robot_roslaunch-check_launch: robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/build.make

.PHONY : _run_tests_robot_roslaunch-check_launch

# Rule to build all files generated by this target.
robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/build: _run_tests_robot_roslaunch-check_launch

.PHONY : robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/build

robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/clean:
	cd /home/nvidia/projects/rosproject/build/robot && $(CMAKE_COMMAND) -P CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/cmake_clean.cmake
.PHONY : robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/clean

robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/depend:
	cd /home/nvidia/projects/rosproject/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nvidia/projects/rosproject/src /home/nvidia/projects/rosproject/src/robot /home/nvidia/projects/rosproject/build /home/nvidia/projects/rosproject/build/robot /home/nvidia/projects/rosproject/build/robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : robot/CMakeFiles/_run_tests_robot_roslaunch-check_launch.dir/depend

