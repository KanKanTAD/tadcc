
import bazel_base.WorkClient

class Deleter(bazel_base.WorkClient.WorkClient):
    @abstractmethod
    def by_index(self, idx):
        pass
        
    def __init__(self):
        super(Deleter, self).__init__()
        pass
    
