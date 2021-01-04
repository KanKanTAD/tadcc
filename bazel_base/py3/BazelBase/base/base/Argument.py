
import Namiable
import Value
import Stringify

class Argument(Namiable.Namiable, Stringify.Stringify):
    def set_value(self, value) -> None:
        self.__value= value
        
    def get_value(self) -> Value.Value:
        return self.__value
        
    def stringify(self) -> str:
        res = ''
        name = self.get_name()
        if name != '':
            res += name + ' = '
        value = self.get_value()
        res += value.stringify()
        return res
        
    def __init__(self):
        super(Argument, self).__init__()
        self.__value = Value.Value()
        pass
    
