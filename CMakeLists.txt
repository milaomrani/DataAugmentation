cmake_minimum_required(VERSION 3.0.0)
project(Data_Augmentation VERSION 0.1.0)

include(CTest)
enable_testing()

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_subdirectory("E:\\Libraries\\dlib-19.24\\dlib-19.24" dlib_build)

# Set the output directory for the executable
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(Data_Augmentation data_aug.cpp)
target_link_libraries(Data_Augmentation ${OpenCV_LIBS} ${dlib_LIBRARIES} dlib::dlib)


set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
