
import base.CallMeta
import base.Stringify

class BazelBuild(base.Stringify.Stringify):
    def __init__(self):
        super(BazelBuild, self).__init__()
        self.__call_metis = list()
        pass
    
