
import CallMeta
import Namiable

from Typing import List,Tuple,Set,Dict
class Target(CallMeta.CallMeta, Namiable.Namiable):
    def get_deps(self) -> Tuple[int,Argument]:
        arg_list = self.get_arglist()
        for i in range(len(arg_list)):
            arg = arg_list[i]
            if arg.get_name() == 'deps':
                return i,arg
        return -1,None 
            
        
    def __init__(self, proto: CallMeta.CallMeta):
        super(Target, self).__init__()
        self.__proto = None
        self.__proto = proto
        
    
