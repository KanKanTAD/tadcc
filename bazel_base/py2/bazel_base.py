class Notiable:
    def __init__(self):
        self.__note = ''

    def setNote(self, note):
        self.__note = s

    def getNote(self):
        return self.__note


class Namiable:
    def __init__(self):
        self.__name = ''

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Func(Notiable, Namiable):
    pass


class Attribute(Notiable, Namiable):
    def __init__(self, name, multi=False):
        pass

    def isMulti(self):
        pass

    def getContent(self):
        pass


class Target:
    def getName(self):
        pass

    def addAttr(self, attr):
        pass

    def listAttr(self):
        pass

    def searchAttrByName(self, pattern: str) -> List[Attribute]:
        pass

    def selectAttrByName(self, name: str) -> Attribute:
        pass

    def selectAttrByContent(self, content: str) -> List[Attribute]:
        pass

    def searchAttrByContent(self, pattern: str) -> List[Attribute]:
        pass


class BazelBuild:
    def load(self, file_path):
        pass

    def create(self) -> str:
        pass

    def saveAsFile(self, file_path):
        pass

    def listTargets(self):
        pass

    def getTargets(self, name=None, keywords=None):
        pass

    # target:Target
    def addTarget(self, target):
        pass
