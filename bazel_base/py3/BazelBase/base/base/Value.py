
import Stringify

class Value(Stringify.Stringify):
    @abstractmethod
    def get_valuetype(self) -> int:
        pass
        
    def __init__(self):
        super(Value, self).__init__()
        pass
    
