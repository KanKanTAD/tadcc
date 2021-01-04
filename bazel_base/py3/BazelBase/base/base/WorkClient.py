
import base.BazelBuild

class WorkClient(object):
    def set_bazelbuild(self, build: base.BazelBuild.BazelBuild) -> void:
        self.__build = build
        
    def __init__(self):
        self.__build = None
        pass
    
