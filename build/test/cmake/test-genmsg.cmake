# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "test: 1 messages, 1 services")

set(MSG_I_FLAGS "-Itest:/home/nvidia/projects/rosproject/src/test/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(test_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_custom_target(_test_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test" "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" ""
)

get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_custom_target(_test_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "test" "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(test
  "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test
)

### Generating Services
_generate_srv_cpp(test
  "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test
)

### Generating Module File
_generate_module_cpp(test
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(test_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(test_generate_messages test_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_dependencies(test_generate_messages_cpp _test_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_dependencies(test_generate_messages_cpp _test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_gencpp)
add_dependencies(test_gencpp test_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(test
  "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test
)

### Generating Services
_generate_srv_eus(test
  "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test
)

### Generating Module File
_generate_module_eus(test
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(test_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(test_generate_messages test_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_dependencies(test_generate_messages_eus _test_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_dependencies(test_generate_messages_eus _test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_geneus)
add_dependencies(test_geneus test_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(test
  "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test
)

### Generating Services
_generate_srv_lisp(test
  "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test
)

### Generating Module File
_generate_module_lisp(test
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(test_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(test_generate_messages test_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_dependencies(test_generate_messages_lisp _test_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_dependencies(test_generate_messages_lisp _test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_genlisp)
add_dependencies(test_genlisp test_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(test
  "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test
)

### Generating Services
_generate_srv_nodejs(test
  "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test
)

### Generating Module File
_generate_module_nodejs(test
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(test_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(test_generate_messages test_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_dependencies(test_generate_messages_nodejs _test_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_dependencies(test_generate_messages_nodejs _test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_gennodejs)
add_dependencies(test_gennodejs test_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(test
  "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test
)

### Generating Services
_generate_srv_py(test
  "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test
)

### Generating Module File
_generate_module_py(test
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(test_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(test_generate_messages test_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/msg/SentMessage.msg" NAME_WE)
add_dependencies(test_generate_messages_py _test_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/nvidia/projects/rosproject/src/test/srv/RandomNumber.srv" NAME_WE)
add_dependencies(test_generate_messages_py _test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(test_genpy)
add_dependencies(test_genpy test_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS test_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/test
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(test_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/test
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(test_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/test
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(test_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/test
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(test_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/test
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(test_generate_messages_py std_msgs_generate_messages_py)
endif()
