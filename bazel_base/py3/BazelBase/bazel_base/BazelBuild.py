
import bazel_base.CallMeta
import bazel_base.Stringify

class BazelBuild(bazel_base.Stringify.Stringify):
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
