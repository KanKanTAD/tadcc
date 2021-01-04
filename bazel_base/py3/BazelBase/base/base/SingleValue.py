
import Value

class SingleValue(Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Single
        
    def value(self) -> str:
        return self.__value
        
    def __init__(self, value: str):
        super(SingleValue, self).__init__()
        self.__value = value
        
    def stringify(self) -> str:
        return self.__value
        
    
