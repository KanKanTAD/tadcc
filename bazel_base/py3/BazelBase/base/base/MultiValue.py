
import Value

class MultiValue(Value.Value):
    def get_valuetype(self) -> int:
        return ValueType.Multi
        
    def list(self):
        pass
        
    def init_by_singlevalues(self, values) -> None:
        pass
        
    def __init__(self, values):
        super(MultiValue, self).__init__()
        self.__values = values
        
    def stringify(self) -> str:
        res = '['
        val_list = self.list()
        val = ', \n'.join([v for v in val_list])
        res += val
        res += ']'
        return res
        
    
