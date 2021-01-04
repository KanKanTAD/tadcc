
import base.Stringify

class Value(base.Stringify.Stringify):
    @abstractmethod
    def get_source() -> string:
        pass
        
    @abstractmethod
    def get_valuetype(self):
        pass
        
    def __init__(self):
        super(Value, self).__init__()
        pass
    
