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

# Include any dependencies generated for this target.
include chip_bldc_driver/CMakeFiles/crc16.dir/depend.make

# Include the progress variables for this target.
include chip_bldc_driver/CMakeFiles/crc16.dir/progress.make

# Include the compile flags for this target's objects.
include chip_bldc_driver/CMakeFiles/crc16.dir/flags.make

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o: chip_bldc_driver/CMakeFiles/crc16.dir/flags.make
chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o: /home/nvidia/projects/rosproject/src/chip_bldc_driver/src/crc16.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nvidia/projects/rosproject/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o"
	cd /home/nvidia/projects/rosproject/build/chip_bldc_driver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/crc16.dir/src/crc16.cpp.o -c /home/nvidia/projects/rosproject/src/chip_bldc_driver/src/crc16.cpp

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/crc16.dir/src/crc16.cpp.i"
	cd /home/nvidia/projects/rosproject/build/chip_bldc_driver && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nvidia/projects/rosproject/src/chip_bldc_driver/src/crc16.cpp > CMakeFiles/crc16.dir/src/crc16.cpp.i

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/crc16.dir/src/crc16.cpp.s"
	cd /home/nvidia/projects/rosproject/build/chip_bldc_driver && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nvidia/projects/rosproject/src/chip_bldc_driver/src/crc16.cpp -o CMakeFiles/crc16.dir/src/crc16.cpp.s

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.requires:

.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.requires

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.provides: chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.requires
	$(MAKE) -f chip_bldc_driver/CMakeFiles/crc16.dir/build.make chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.provides.build
.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.provides

chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.provides.build: chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o


# Object files for target crc16
crc16_OBJECTS = \
"CMakeFiles/crc16.dir/src/crc16.cpp.o"

# External object files for target crc16
crc16_EXTERNAL_OBJECTS =

/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: chip_bldc_driver/CMakeFiles/crc16.dir/build.make
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/libroscpp.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_filesystem.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/librosconsole.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/liblog4cxx.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_regex.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /home/nvidia/projects/rosproject/devel/lib/libserial.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/librt.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/librostime.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /opt/ros/melodic/lib/libcpp_common.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_system.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_thread.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_chrono.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_date_time.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libboost_atomic.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libpthread.so
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: /usr/lib/aarch64-linux-gnu/libconsole_bridge.so.0.4
/home/nvidia/projects/rosproject/devel/lib/libcrc16.so: chip_bldc_driver/CMakeFiles/crc16.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nvidia/projects/rosproject/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library /home/nvidia/projects/rosproject/devel/lib/libcrc16.so"
	cd /home/nvidia/projects/rosproject/build/chip_bldc_driver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/crc16.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
chip_bldc_driver/CMakeFiles/crc16.dir/build: /home/nvidia/projects/rosproject/devel/lib/libcrc16.so

.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/build

chip_bldc_driver/CMakeFiles/crc16.dir/requires: chip_bldc_driver/CMakeFiles/crc16.dir/src/crc16.cpp.o.requires

.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/requires

chip_bldc_driver/CMakeFiles/crc16.dir/clean:
	cd /home/nvidia/projects/rosproject/build/chip_bldc_driver && $(CMAKE_COMMAND) -P CMakeFiles/crc16.dir/cmake_clean.cmake
.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/clean

chip_bldc_driver/CMakeFiles/crc16.dir/depend:
	cd /home/nvidia/projects/rosproject/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nvidia/projects/rosproject/src /home/nvidia/projects/rosproject/src/chip_bldc_driver /home/nvidia/projects/rosproject/build /home/nvidia/projects/rosproject/build/chip_bldc_driver /home/nvidia/projects/rosproject/build/chip_bldc_driver/CMakeFiles/crc16.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : chip_bldc_driver/CMakeFiles/crc16.dir/depend

