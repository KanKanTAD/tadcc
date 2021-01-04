
import base.WorkClient

class Deleter(base.WorkClient.WorkClient):
    @abstractmethod
    def by_index(idx: int) -> bool:
        pass
        
    def __init__(self):
        super(Deleter, self).__init__()
        pass
    
