
import CallMeta
import Stringify

from typing import List,Set,Tuple,Dict
class BazelBuild(Stringify.Stringify):
    def set_call_metis(self, call_metis) -> None:
        self.__call_metis = call_metis
        
    def get_call_metis(self):
        return self.__call_metis
        
    def stringify(self) -> str:
        metis = self.get_call_metis()
        return '' + str(len(metis))
        
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
