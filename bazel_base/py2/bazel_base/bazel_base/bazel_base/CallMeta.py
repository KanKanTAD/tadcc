
import bazel_base.Com


class CallMeta(bazel_base.Com.Com):
    def stringify(self, spaces=''):
        res = spaces + str(self.name) + '('
        body = ', '.join([c.stringify(spaces) for c in self.children])
        res += body
        res += spaces + ')'
        return res

    def __init__(self):
        super(CallMeta, self).__init__()
        pass
