cmake_minimum_required(VERSION 3.0.0)
project(bazel_base)

set(ANTRL_GEN_PATH ./dist)
set(BAZEL_BASE_PATH ./bazel_base/bazel_base)


include_directories(${ANTRL_GEN_PATH} ${BAZEL_BASE_PATH}/include)

set(SRC 
	${ANTRL_GEN_PATH}/BazelBuildBaseVisitor.cpp
	${ANTRL_GEN_PATH}/BazelBuildBaseListener.cpp
	${ANTRL_GEN_PATH}/BazelBuildLexer.cpp
	${ANTRL_GEN_PATH}/BazelBuildParser.cpp
	${ANTRL_GEN_PATH}/BazelBuildVisitor.cpp
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

add_executable(example example.cc ${SRC})
