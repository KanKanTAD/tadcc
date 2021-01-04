
import base.Namiable
import base.Value

from typing import List,Set,Dict,Tuple
class Argument(base.Namiable.Namiable):
    def set_value(self: Argument, value: base.Value.Value) -> void:
        self.__value= value
        
    def get_value(self: Argument) -> base.Value.Value:
        return self.__value
        
    def __init__(self):
        super(Argument, self).__init__()
        self.__value = base.Value.Value()
        pass
    
