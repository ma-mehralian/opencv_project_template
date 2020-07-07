cmake_minimum_required(VERSION 3.6)
project(roi_grabber)

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

#==== ENGINE
add_library(${PROJECT_NAME}
    src/roi_grabber.cpp
)
target_include_directories(${PROJECT_NAME}
    PRIVATE src
    PUBLIC include
    PRIVATE ${OpenCV_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}
    PUBLIC ${OpenCV_LIBS}
)

#==== CONSOLE APP
add_executable(${PROJECT_NAME}_test
    tests/main.cpp
)
target_link_libraries(${PROJECT_NAME}_test
    PRIVATE ${PROJECT_NAME}
)

#==== MSVC folder structure
set_target_properties(
    ${PROJECT_NAME}
    ${PROJECT_NAME}_test
    PROPERTIES FOLDER "modules/${PROJECT_NAME}")
