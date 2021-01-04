
import base.CallMeta
import base.Namiable

from Typing import List,Tuple,Set,Dict
class Target(base.CallMeta.CallMeta, base.Namiable.Namiable):
    def get_deps(self: base.CallMeta.CallMeta) -> Tuple[int,Argument]:
        arg_list = self.get_arglist()
        for i in range(len(arg_list)):
            arg = arg_list[i]
            if arg.get_name() == 'deps':
                return i,arg
        return -1,None 
            
        
    def __init__(self: Target, proto: base.CallMeta.CallMeta):
        super(Target, self).__init__()
        self.__proto = None
        self.__proto = proto
        
    
