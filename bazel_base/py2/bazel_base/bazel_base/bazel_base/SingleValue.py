
import bazel_base.Value

class SingleValue(bazel_base.Value.Value):
    def stringify(self, spaces = ''):
    return '' if self.value is None else str(self.value)
    
        
    def __init__(self):
        super(SingleValue, self).__init__()
        self.value = ''
        pass
    
