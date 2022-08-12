cmake_minimum_required(VERSION 3.6)
project(roi_grabber)

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

# Module
add_library(${PROJECT_NAME}
    src/roi_grabber.cpp
)
target_include_directories(${PROJECT_NAME}
    PRIVATE src
    PUBLIC include
    PUBLIC ${OpenCV_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}
    PUBLIC ${OpenCV_LIBS}
)

# examples
add_executable(${PROJECT_NAME}_example
    examples/main.cpp
)
target_link_libraries(${PROJECT_NAME}_example
    PRIVATE ${PROJECT_NAME}
)

# folder structure
set_target_properties(
    ${PROJECT_NAME}
    ${PROJECT_NAME}_example
    PROPERTIES FOLDER "modules/${PROJECT_NAME}")
