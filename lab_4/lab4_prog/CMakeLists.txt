cmake_minimum_required(VERSION 3.17)
project(prog_ef1t)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS -pthread)

add_executable(prog_ef1t main.cpp ordinary.cpp ordinary.h parallelQueue.cpp parallelQueue.h parallelDistribution.cpp parallelDistribution.h)