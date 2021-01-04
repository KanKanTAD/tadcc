
import base.WorkClient
import base.CallMeta

from Typing import List,Set,Tuple
class Searcher(base.WorkClient.WorkClient):
    def __len__(self) -> int:
        return len(self.__build.get_call_metis())
        
    def list(self: Searcher) -> List[CallMeta]:
        pass
        
    def by_index(self: Searcher, idx: int) -> base.CallMeta.CallMeta:
        ls = self.__build.get_call_metis()
        idx = idx if idx >= 0 else len(ls) + idx 
        if not (0 <= idx < len(ls)):
            return None 
        return ls[idx]
            
        
    def __init__(self):
        super(Searcher, self).__init__()
        pass
    
