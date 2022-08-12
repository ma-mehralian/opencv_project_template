cmake_minimum_required(VERSION 3.6)
project(ocv_project)

set(CMAKE_VERBOSE_MAKEFILE on)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set_property(GLOBAL PROPERTY USE_FOLDERS TRUE)

# Set output paths
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "$<$<CONFIG:Debug>:debug>$<$<NOT:$<CONFIG:Debug>>:release>" CACHE STRING "" FORCE)
endif()
set(CMAKE_BINARY_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../${PROJECT_NAME}_build-${CMAKE_BUILD_TYPE}")
if (WIN32)
    set(CMAKE_BINARY_DIR "${CMAKE_BINARY_DIR}-win")
endif (WIN32)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)


# Set Library Paths (OpenCV, ...)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")
set(REFS_PATH "${CMAKE_SOURCE_DIR}/../refs")

if(WIN32)
    set(OpenCV_DIR "${REFS_PATH}/opencv/4.2.0/install-vs2019-x64/x64/vc16/lib")
    set(TF_DIR "${REFS_PATH}/tf/libtensorflow-cpu-windows-x86_64-1.15.0")
else()
    set(OpenCV_DIR "${REFS_PATH}/opencv/4.2.0/install-gcc-x86-64/lib/cmake/opencv4")
    set(TF_DIR "${REFS_PATH}/tf/libtensorflow-gpu-linux-x86_64-1.15.0")
endif()


# Project options
macro(MY_OPTION variable description value)
    option(${variable} "${description}" ${value})
    if(${value})
    add_compile_options("-D${variable}")
    endif()
endmacro()
my_option(USE_TF "Use Tensorflow library" OFF)


# List of Apps
add_subdirectory("apps/console_app")


# List of Modules
add_subdirectory("modules/roi_grabber")

