cmake_minimum_required(VERSION 3.6)
project(ocv_project)

#==== set USE_FOLDERS for MSVC
set_property(GLOBAL PROPERTY USE_FOLDERS TRUE)

#==== Set Output paths
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "$<$<CONFIG:Debug>:debug>$<$<NOT:$<CONFIG:Debug>>:release>" CACHE STRING "" FORCE)
endif()
set(CMAKE_BINARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/build-${CMAKE_BUILD_TYPE}$<$<PLATFORM_ID:Windows>:-win>)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)


#==== Set Library Paths (OpenCV, ...)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")
set(REFS_PATH "${CMAKE_SOURCE_DIR}/../refs")

if(WIN32)
    set(OpenCV_DIR "${REFS_PATH}/opencv/4.2.0/install-vs2019-x64/x64/vc16/lib")
else()
    set(OpenCV_DIR "${REFS_PATH}/opencv/4.2.0/install-gcc-x86-64/lib/cmake/opencv4")
endif()

#==== List of Modules
add_subdirectory("modules/roi_grabber")

#==== List of Apps
add_subdirectory("apps/test_app")

