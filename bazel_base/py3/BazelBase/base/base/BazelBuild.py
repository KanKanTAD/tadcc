
import CallMeta
import Stringify

from typing import List,Set,Tuple,Dict
class BazelBuild(Stringify.Stringify):
    def set_call_metis(self, call_metis: List[CallMeta]) -> None:
        self.__call_metis = call_metis
        
    def get_call_metis(self) -> List[CallMeta]:
        return self.__call_metis
        
    def stringify(self) -> str:
        pass
        
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
