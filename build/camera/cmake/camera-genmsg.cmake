# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "camera: 1 messages, 1 services")

set(MSG_I_FLAGS "-Icamera:/home/nvidia/projects/rosproject/src/camera/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(camera_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_custom_target(_camera_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "camera" "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" ""
)

get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_custom_target(_camera_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "camera" "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(camera
  "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera
)

### Generating Services
_generate_srv_cpp(camera
  "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera
)

### Generating Module File
_generate_module_cpp(camera
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(camera_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(camera_generate_messages camera_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_dependencies(camera_generate_messages_cpp _camera_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_dependencies(camera_generate_messages_cpp _camera_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_gencpp)
add_dependencies(camera_gencpp camera_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(camera
  "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera
)

### Generating Services
_generate_srv_eus(camera
  "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera
)

### Generating Module File
_generate_module_eus(camera
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(camera_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(camera_generate_messages camera_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_dependencies(camera_generate_messages_eus _camera_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_dependencies(camera_generate_messages_eus _camera_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_geneus)
add_dependencies(camera_geneus camera_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(camera
  "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera
)

### Generating Services
_generate_srv_lisp(camera
  "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera
)

### Generating Module File
_generate_module_lisp(camera
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(camera_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(camera_generate_messages camera_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_dependencies(camera_generate_messages_lisp _camera_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_dependencies(camera_generate_messages_lisp _camera_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_genlisp)
add_dependencies(camera_genlisp camera_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(camera
  "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera
)

### Generating Services
_generate_srv_nodejs(camera
  "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera
)

### Generating Module File
_generate_module_nodejs(camera
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(camera_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(camera_generate_messages camera_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_dependencies(camera_generate_messages_nodejs _camera_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_dependencies(camera_generate_messages_nodejs _camera_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_gennodejs)
add_dependencies(camera_gennodejs camera_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(camera
  "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera
)

### Generating Services
_generate_srv_py(camera
  "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera
)

### Generating Module File
_generate_module_py(camera
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(camera_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(camera_generate_messages camera_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/msg/SentMessage.msg" NAME_WE)
add_dependencies(camera_generate_messages_py _camera_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/camera/srv/RandomNumber.srv" NAME_WE)
add_dependencies(camera_generate_messages_py _camera_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_genpy)
add_dependencies(camera_genpy camera_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(camera_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(camera_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(camera_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(camera_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(camera_generate_messages_py std_msgs_generate_messages_py)
endif()
