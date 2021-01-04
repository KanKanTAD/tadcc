
import base.Argment
import base.Stringify

class CallMeta(base.Stringify.Stringify):
    def __init__(self):
        super(CallMeta, self).__init__()
        self.__arg_list = list()
        pass
    
