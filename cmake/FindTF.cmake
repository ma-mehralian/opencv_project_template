# - Try to find TensorFlow library in TF_DIR
# Once done this will define
#
# TF_FOUND - system has TF
# TF_INCLUDE_DIR - the TF include directory
# TF_LIBRARIES - Link these to use TF
#

if (TF_LIBRARIES AND TF_INCLUDE_DIR)
    # in cache already
    set(TF_FOUND TRUE)
else (TF_LIBRARIES AND TF_INCLUDE_DIR)

    find_path(TF_INCLUDE_DIR
        NAMES tensorflow/c/c_api.h
        PATHS ${TF_DIR}/include 
        )

    find_library(TF_LIBRARIES
        NAMES tensorflow
        PATHS ${TF_DIR}/lib
        )

    if (TF_INCLUDE_DIR AND TF_LIBRARIES)
        set(TF_FOUND TRUE)
        message(STATUS "Found TensorFlow in ${TF_DIR}")
    else ()
        message(FATAL_ERROR "Could not find TensorFlow in ${TF_DIR}")
    endif ()

endif (TF_LIBRARIES AND TF_INCLUDE_DIR)

