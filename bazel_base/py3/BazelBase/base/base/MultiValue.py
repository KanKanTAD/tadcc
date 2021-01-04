
import base.Value

class MultiValue(base.Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Multi
        
    def list(self: MultiValue) -> List[str]:
        pass
        
    def init_by_singlevalues(self: MultiValue, values: List[SingleValue]) -> void:
        pass
        
    def stringify() -> str:
        pass
        
    def __init__(self: MultiValue, values: List[str]):
        super(MultiValue, self).__init__()
        self.__values = values
        
    
