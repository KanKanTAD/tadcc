cmake_minimum_required(VERSION 3.0.0)
project(bazel_base)

set(CMAKE_CXX_STANDARD 17)

add_executable(main ./main.cc ./value.cc)
