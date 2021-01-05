
import bazel_base.Value


class MultiValue(bazel_base.Value.Value):
    def stringify(self, spaces=''):
        _spaces = spaces + (' '*2)
        split = '\n'+_spaces
        res = '['+split
        res += split.join([c.stringify() for c in self.children])
        res += spaces + ']'
        return res

    def __init__(self):
        super(MultiValue, self).__init__()
        pass
