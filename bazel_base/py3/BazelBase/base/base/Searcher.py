
import base.WorkClient

class Searcher(base.WorkClient.WorkClient):
    @abstractmethod
    def __len__(self):
        pass
        
    def __init__(self):
        super(Searcher, self).__init__()
        pass
    
