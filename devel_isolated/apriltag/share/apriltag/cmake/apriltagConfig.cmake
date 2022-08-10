
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was apriltagConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

if(NOT MSVC)
  include(CMakeFindDependencyMacro)
  find_dependency(Threads)
endif()

include("${CMAKE_CURRENT_LIST_DIR}/apriltagTargets.cmake")
check_required_components("apriltag")

if(NOT TARGET apriltag AND ${CMAKE_VERSION} VERSION_GREATER "3.10.99")
  # Make imported target globally visible in order to create an ALIAS
  # IMPORTED_GLOBAL is only available in CMake 3.11+
  set_target_properties(apriltag::apriltag PROPERTIES IMPORTED_GLOBAL TRUE)
  # Create alias for backwards compatibility with 3.1.2 and earlier (will be removed in the future - please migrate to apriltag::apriltag)
  add_library(apriltag ALIAS apriltag::apriltag)
endif()
