cmake_minimum_required(VERSION 3.0.0)
project(bazel_base)

SET (CMAKE_C_COMPILER             "/usr/local/bin/gcc")
SET (CMAKE_C_FLAGS                "-Wall -std=c99")
SET (CMAKE_C_FLAGS_DEBUG          "-g")
SET (CMAKE_C_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
SET (CMAKE_C_FLAGS_RELEASE        "-O4 -DNDEBUG")
SET (CMAKE_C_FLAGS_RELWITHDEBINFO "-O2 -g")

SET (CMAKE_CXX_COMPILER             "/usr/local/bin/g++")
SET (CMAKE_CXX_FLAGS                "-Wall")
SET (CMAKE_CXX_FLAGS_DEBUG          "-g")
SET (CMAKE_CXX_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
SET (CMAKE_CXX_FLAGS_RELEASE        "-O4 -DNDEBUG")
SET (CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g")
SET (CMAKE_CXX_STANDARD 20)

set(ANTRL_GEN_PATH ./dist)
set(BAZEL_BASE_PATH ./bazel_base/bazel_base)
set(ANTRL_RUNTIME_INCLUDE /usr/local/include/antlr4-runtime/)

set(ANTRL_RUNTIME_LINK libantlr4-runtime.a)


include_directories(
	${ANTRL_GEN_PATH}
	${BAZEL_BASE_PATH}/include
	${ANTRL_RUNTIME_INCLUDE}
)

set(Arch_SRC
	${BAZEL_BASE_PATH}/src/Argument.cpp
	${BAZEL_BASE_PATH}/src/BazelBuild.cpp
	${BAZEL_BASE_PATH}/src/CallMeta.cpp
	${BAZEL_BASE_PATH}/src/Com.cpp
	${BAZEL_BASE_PATH}/src/ComContext.cpp
	${BAZEL_BASE_PATH}/src/Erasible.cpp
	${BAZEL_BASE_PATH}/src/Identify.cpp
	${BAZEL_BASE_PATH}/src/MultiValue.cpp
	${BAZEL_BASE_PATH}/src/Namiable.cpp
	${BAZEL_BASE_PATH}/src/Removible.cpp
	${BAZEL_BASE_PATH}/src/SingleValue.cpp
	${BAZEL_BASE_PATH}/src/Stringify.cpp
	${BAZEL_BASE_PATH}/src/Treify.cpp
	${BAZEL_BASE_PATH}/src/Value.cpp
	)
set(Parser_SRC 
	${ANTRL_GEN_PATH}/BazelBuildBaseVisitor.cpp
	${ANTRL_GEN_PATH}/BazelBuildBaseListener.cpp
	${ANTRL_GEN_PATH}/BazelBuildLexer.cpp
	${ANTRL_GEN_PATH}/BazelBuildParser.cpp
	${ANTRL_GEN_PATH}/BazelBuildVisitor.cpp
	)

add_executable(example 
	example.cc 
	${Parser_SRC})

target_link_libraries(example 
	${ANTRL_RUNTIME_LINK})
