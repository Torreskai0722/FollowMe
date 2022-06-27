# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "chip_bldc_driver: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ichip_bldc_driver:/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(chip_bldc_driver_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_custom_target(_chip_bldc_driver_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "chip_bldc_driver" "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_custom_target(_chip_bldc_driver_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "chip_bldc_driver" "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_custom_target(_chip_bldc_driver_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "chip_bldc_driver" "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_cpp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_cpp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver
)

### Generating Services

### Generating Module File
_generate_module_cpp(chip_bldc_driver
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(chip_bldc_driver_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(chip_bldc_driver_generate_messages chip_bldc_driver_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_cpp _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_cpp _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_cpp _chip_bldc_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(chip_bldc_driver_gencpp)
add_dependencies(chip_bldc_driver_gencpp chip_bldc_driver_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS chip_bldc_driver_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_eus(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_eus(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver
)

### Generating Services

### Generating Module File
_generate_module_eus(chip_bldc_driver
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(chip_bldc_driver_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(chip_bldc_driver_generate_messages chip_bldc_driver_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_eus _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_eus _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_eus _chip_bldc_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(chip_bldc_driver_geneus)
add_dependencies(chip_bldc_driver_geneus chip_bldc_driver_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS chip_bldc_driver_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_lisp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_lisp(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver
)

### Generating Services

### Generating Module File
_generate_module_lisp(chip_bldc_driver
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(chip_bldc_driver_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(chip_bldc_driver_generate_messages chip_bldc_driver_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_lisp _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_lisp _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_lisp _chip_bldc_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(chip_bldc_driver_genlisp)
add_dependencies(chip_bldc_driver_genlisp chip_bldc_driver_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS chip_bldc_driver_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_nodejs(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_nodejs(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver
)

### Generating Services

### Generating Module File
_generate_module_nodejs(chip_bldc_driver
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(chip_bldc_driver_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(chip_bldc_driver_generate_messages chip_bldc_driver_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_nodejs _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_nodejs _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_nodejs _chip_bldc_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(chip_bldc_driver_gennodejs)
add_dependencies(chip_bldc_driver_gennodejs chip_bldc_driver_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS chip_bldc_driver_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_py(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver
)
_generate_msg_py(chip_bldc_driver
  "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver
)

### Generating Services

### Generating Module File
_generate_module_py(chip_bldc_driver
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(chip_bldc_driver_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(chip_bldc_driver_generate_messages chip_bldc_driver_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Status.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_py _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Feedback.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_py _chip_bldc_driver_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/chip_bldc_driver/msg/Command.msg" NAME_WE)
add_dependencies(chip_bldc_driver_generate_messages_py _chip_bldc_driver_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(chip_bldc_driver_genpy)
add_dependencies(chip_bldc_driver_genpy chip_bldc_driver_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS chip_bldc_driver_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/chip_bldc_driver
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(chip_bldc_driver_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/chip_bldc_driver
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(chip_bldc_driver_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/chip_bldc_driver
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(chip_bldc_driver_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/chip_bldc_driver
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(chip_bldc_driver_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/chip_bldc_driver
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(chip_bldc_driver_generate_messages_py std_msgs_generate_messages_py)
endif()
