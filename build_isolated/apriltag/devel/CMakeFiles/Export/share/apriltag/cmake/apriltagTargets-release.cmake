#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "apriltag::apriltag" for configuration "Release"
set_property(TARGET apriltag::apriltag APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(apriltag::apriltag PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libapriltag.so.3.2.0"
  IMPORTED_SONAME_RELEASE "libapriltag.so.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS apriltag::apriltag )
list(APPEND _IMPORT_CHECK_FILES_FOR_apriltag::apriltag "${_IMPORT_PREFIX}/lib/libapriltag.so.3.2.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
