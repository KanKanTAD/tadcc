#!/usr/bin/env python

# -*- encoding:utf8 -*-

import bazel_base as bb

build = bb.BazelBuildFactory.createFromFile('./example.BUILD')

deleter = bb.DefaultDeleter(build)

deleter.deep_remove_target(name='mmpaymktmembercardmgrmedi_pb_h')

with open('out.BUILD', 'w') as f:
    f.write(build.stringify())
