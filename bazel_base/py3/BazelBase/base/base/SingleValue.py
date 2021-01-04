
import base.Value

class SingleValue(base.Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Single
        
    def value(self: SingleValue) -> string:
        return self.__value
        
    def stringify() -> str:
        pass
        
    def __init__(self: SingleValue, value: str):
        super(SingleValue, self).__init__()
        self.__value = value
        
    
