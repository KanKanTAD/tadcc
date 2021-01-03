
import bazel_base.Namiable
import bazel_base.Value

class Argment(bazel_base.Namiable.Namiable):
    def __init__(self):
        super(Argment, self).__init__()
        self.__value = bazel_base.Value.Value()
        pass
    
