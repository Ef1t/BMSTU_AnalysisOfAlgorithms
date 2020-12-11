cmake_minimum_required(VERSION 3.17)
project(lab5_prog)

set(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_FLAGS -pthread)

add_executable(lab5_prog main.cpp MyTimer.cpp LinearWork.cpp ConveyorWork.cpp)