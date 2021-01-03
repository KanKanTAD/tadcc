
import bazel_base.Argment
import bazel_base.Stringify

class CallMeta(bazel_base.Stringify.Stringify):
    def __init__(self):
        super(CallMeta, self).__init__()
        self.__arg_list = list()
        pass
    
