
import base.Stringify

class Value(base.Stringify.Stringify):
    def get_source(self: Value) -> str:
        pass
        
    @abstractmethod
    def get_valuetype(self) -> int:
        pass
        
    def set_source(self: Value, source: str) -> void:
        self.__source = source
        
    def __init__(self):
        super(Value, self).__init__()
        pass
    
