
from typing import List,Set,Tuple
import CallMeta
import Stringify

class BazelBuild(Stringify.Stringify):
    def set_call_metis(self: BazelBuild, call_metis: List[CallMeta]) -> void:
        self.__call_metis = call_metis
        
    def get_call_metis(self: BazelBuild) -> List[CallMeta]:
        return self.__call_metis
        
    def stringify() -> str:
        pass
        
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
