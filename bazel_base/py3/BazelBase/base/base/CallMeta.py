
import Argument
import Stringify

from typing import List,Set,Tuple,Dict
class CallMeta(Stringify.Stringify):
    def get_funcname(self):
        return self.__func_name
        
    def set_funcname(self, name: str) -> None:
        self.__func_name = name
        
    def get_arglist(self) -> List:
        return self.__arg_list
        
    def set_arglist(self, arg_list) -> None:
        self.__arg_list = arg_list
        
    def stringify(self) -> str:
        res = '' + self.get_funcname()
        res += '(\n'
        arg_list = self.get_arglist()
        arg = [a.stringify() for a in arg_list].join(', \n')
        res += ')'
        return res
        
    def __init__(self):
        super(CallMeta, self).__init__()
        self.__arg_list = list()
        pass
    
