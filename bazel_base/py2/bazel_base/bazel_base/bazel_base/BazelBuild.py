
import bazel_base.Com


class BazelBuild(bazel_base.Com.Com):
    def init_from_file(self, file_path):
        pass

    def stringify(self, spaces=''):
        split = '\n'+spaces
        return spaces + (split.join([c.stringify() for c in self.children]))

    def __init__(self):
        super(BazelBuild, self).__init__()
        pass
