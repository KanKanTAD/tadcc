#!/usr/bin/env sh
java -jar ../../tools/antlr-4.9-complete.jar -Dlanguage=Python2 ./BazelBuild.g4 -o dist -visitor
