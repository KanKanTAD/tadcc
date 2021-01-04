
from Typing import List,Set,Tuple
import base.CallMeta
import base.Stringify

class BazelBuild(base.Stringify.Stringify):
    def set_call_metis(self: BazelBuild, call_metis: List[CallMeta]) -> void:
        self.__call_metis = call_metis
        
    def get_call_metis(self: BazelBuild) -> List[CallMeta]:
        return self.__call_metis
        
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
