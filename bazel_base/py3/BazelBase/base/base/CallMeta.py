
import base.Argment
import base.Stringify

from typing import List,Set,Tuple,Dict
class CallMeta(base.Stringify.Stringify):
    def get_funcname():
        pass
        
    def set_funcname(self: CallMeta, name: str) -> void:
        self.__func_name = name
        
    def get_arglist(self: CallMeta) -> List[Argument]:
        return self.__arg_list
        
    def set_arglist(self: CallMeta, arg_list: List[Argument]) -> void:
        self.__arg_list = arg_list
        
    def __init__(self):
        super(CallMeta, self).__init__()
        self.__arg_list = list()
        pass
    
