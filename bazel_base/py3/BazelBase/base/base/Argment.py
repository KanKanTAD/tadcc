
import Namiable
import Value

from typing import List,Set,Dict,Tuple
class Argument(Namiable.Namiable):
    def set_value(self, value: Value.Value) -> None:
        self.__value= value
        
    def get_value(self) -> Value.Value:
        return self.__value
        
    def __init__(self):
        super(Argument, self).__init__()
        self.__value = Value.Value()
        pass
    
