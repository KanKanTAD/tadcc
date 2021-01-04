
import base.Value

class SingleValue(base.Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Single
        
    def value(self: SingleValue) -> string:
        return self.__value
        
    def __init__(self):
        super(SingleValue, self).__init__()
        pass
    
