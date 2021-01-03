
import bazel_base.Stringify

class Value(bazel_base.Stringify.Stringify):
    @abstractmethod
    def get_source(self):
        pass
        
    @abstractmethod
    def get_valuetype(self):
        pass
        
    def __init__(self):
        super(Value, self).__init__()
        pass
    
