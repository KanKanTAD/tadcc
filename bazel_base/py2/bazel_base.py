class Stringible:
    def stringify(self, spaces=2):
        pass


class Stmt(Stringible):

    def getType(self):
        pass


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


class Action(Stmt, Notiable, Namiable):
    def __init__(self, name, args=[]):
        self.setName(name)
        self.__args = args[:]

    def stringify(self, spaces=2):
        args = ', '.join(self.__args)
        res = '' + self.getName() + '('+args+')'
        return res


class Attribute(Notiable, Namiable, Stringible):
    def __init__(self, name, values=[]):
        self.setName(name)
        self.__values = values[:]

    def isMulti(self):
        return len(self.__values) > 1

    def getContent(self):
        pass

    def stringify(self, spaces=2):
        atp = ' ' * spaces
        tab = atp + (' '*2)
        s = atp + self.getName() + ' = '
        if self.isMulti():
            s += '['
        s += ',\n'.join(self.__values)
        if self.isMulti():
            s += atp + ']'
        return s


class Rule(Namiable):
    def __init__(self, name):
        pass


class Target:
    def __init__(self, rule, attrs=[]):
        self.__rule = rule
        self.__attrs = attrs
        self.__init_name()

    def __init_name(self):
        for attr in self.__attrs:
            if attr.getName() == 'name':
                self.setName(attr.getContent[1:-1])
                break

    def stringify(self, spaces=2):
        tab = ''
        s = '' + self.__rule.getName() + '(\n'
        tab += ' ' * spaces
        for attr in self.__attrs:
            s += tab + attr.stringify(spaces+spaces) + '\n'
        s += ')'
        return s

    def addAttr(self, attr):
        pass

    def listAttr(self):
        pass

    def searchAttrByName(self, pattern):
        pass

    def selectAttrByName(self, name):
        pass

    def selectAttrByContent(self, content):
        pass

    def searchAttrByContent(self, pattern):
        pass


class BazelBuild:
    def load(self, file_path):
        pass

    def create(self):
        pass

    def saveAsFile(self, file_path):
        pass

    def listStmt(self):
        pass

    def listTargets(self):
        pass

    def getTargets(self, name=None, keywords=None):
        pass

    # target:Target
    def addTarget(self, target):
        pass
