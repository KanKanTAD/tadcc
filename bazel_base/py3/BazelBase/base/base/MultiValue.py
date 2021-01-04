
import base.Value

class MultiValue(base.Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Multi
        
    def list(self: MultiValue) -> List[str]:
        pass
        
    def __init__(self):
        super(MultiValue, self).__init__()
        pass
    
