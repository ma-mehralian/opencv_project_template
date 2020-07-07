cmake_minimum_required(VERSION 3.6)
project(test_app)

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

#==== CONSOLE APP
add_executable(${PROJECT_NAME}
    src/main.cpp
)
target_include_directories(${PROJECT_NAME}
    PRIVATE ${OpenCV_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}
    roi_grabber ${OpenCV_LIBS}
)
#==== MSVC folder structure
set_target_properties(
    ${PROJECT_NAME}
    PROPERTIES FOLDER "apps/${PROJECT_NAME}")
