
import Argment
import Stringify

from typing import List,Set,Tuple,Dict
class CallMeta(Stringify.Stringify):
    def get_funcname(self):
        pass
        
    def set_funcname(self, name: str) -> void:
        self.__func_name = name
        
    def get_arglist(self) -> List[Argument]:
        return self.__arg_list
        
    def set_arglist(self, arg_list: List[Argument]) -> void:
        self.__arg_list = arg_list
        
    def stringify(self) -> str:
        pass
        
    def __init__(self):
        super(CallMeta, self).__init__()
        self.__arg_list = list()
        pass
    
