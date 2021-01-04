
import WorkClient

class Deleter(WorkClient.WorkClient):
    def by_index(self, idx) -> bool:
        ls = self.__build.get_call_metis()
        idx = idx if idx >= 0 else len(ls) + idx 
        if not (0 <= idx < len(ls)):
            return False 
        del ls[idx] 
        return True 
        
    def __init__(self):
        super(Deleter, self).__init__()
        pass
    
