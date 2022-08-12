cmake_minimum_required(VERSION 3.6)
project(console_app)

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

add_executable(${PROJECT_NAME}
    src/main.cpp
)
target_link_libraries(${PROJECT_NAME}
    roi_grabber
)

# Folder structure
set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER "apps/${PROJECT_NAME}")
