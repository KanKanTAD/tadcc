
import Value

class MultiValue(Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Multi
        
    def list(self) -> List[str]:
        pass
        
    def init_by_singlevalues(self, values: List[SingleValue]) -> None:
        pass
        
    def __init__(self, values: List[str]):
        super(MultiValue, self).__init__()
        self.__values = values
        
    def stringify(self) -> str:
        pass
        
    
