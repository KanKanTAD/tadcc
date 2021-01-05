
import bazel_base.Com

class Argument(bazel_base.Com.Com):
    def stringify(self, spaces = ''):
    res = ''+spaces
    name = '' if self.name is None else str(self.name)
    _spaces = spaces + (' '*2)
    if name != '':
        res += '\n'+spaces 
        res += name + ' = '
    if self.children is None or len(self.children) <= 0:
        return spaces 
    child = self.children[0]
    res += child.stringify(_spaces)
    return res
    
        
    def __init__(self):
        super(Argument, self).__init__()
        pass
    
