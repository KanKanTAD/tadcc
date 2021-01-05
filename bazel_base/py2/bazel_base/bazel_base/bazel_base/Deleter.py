
import bazel_base.BazelBuild

class Deleter(object):
    def __init__(self, build):
        self.build = None
    self.build = build
        
    def remove_target(self, name):
        pass
        
    def deep_remove_target(self, name):
        pass
        
    def remove_depend(self, key):
        pass
        
    
