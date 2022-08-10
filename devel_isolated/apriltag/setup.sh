#!/usr/bin/env sh
# generated from catkin.builder Python module

# remember type of shell if not already set
if [ -z "$CATKIN_SHELL" ]; then
  CATKIN_SHELL=sh
fi
# detect if running on Darwin platform
_UNAME=`uname -s`
IS_DARWIN=0
if [ "$_UNAME" = "Darwin" ]; then
  IS_DARWIN=1
fi

# Prepend to the environment
export CMAKE_PREFIX_PATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag:$CMAKE_PREFIX_PATH"
if [ $IS_DARWIN -eq 0 ]; then
  export LD_LIBRARY_PATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib:/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib/aarch64-linux-gnu:$LD_LIBRARY_PATH"
else
  export DYLD_LIBRARY_PATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib:/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib/aarch64-linux-gnu:$DYLD_LIBRARY_PATH"
fi
export PATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag/bin:$PATH"
export PKG_CONFIG_PATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib/pkgconfig:/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib/aarch64-linux-gnu/pkgconfig:$PKG_CONFIG_PATH"
export PYTHONPATH="/home/nvidia/projects/rosproject/devel_isolated/apriltag/lib/python2.7/dist-packages:$PYTHONPATH"
