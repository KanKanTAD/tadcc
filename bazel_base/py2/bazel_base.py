import antlr4 as antlr
from dist.BazelBuildLexer import BazelBuildLexer
from dist.BazelBuildParser import BazelBuildParser
from dist.BazelBuildVisitor import BazelBuildVisitor


class Namiable:
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Commentable:
    def set_comment(self, comment):
        self.__comment = comment

    def get_comment(self):
        return self.__comment


class Stringify:
    def stringify(self, spaces=2):
        return self.__str__()


class Searcher:
    pass


class Deleter:
    pass


class Multible:
    def is_multi(self):
        return self.__multi

    def be_multi(self):
        self.__multi = True

    def not_multi(self):
        self.__multi = False


class Argument(Namiable, Multible, Stringify):
    def __init__(self, name='', isMulti=False, values=[]):
        self.set_name(name)
        if isMulti:
            self.be_multi()
        else:
            self.not_multi()
        self.__values = values

    def stringify(self):
        res = ''
        if len(name) > 0:
            res += self.get_name() + ' = '
        values = ', '.join(self.__values)
        if self.is_multi():
            values = '['+values+']'
        return res + value


class Stmt(Stringify):
    def get_type(self):
        pass


class NoteExp(Stmt):
    def __init__(self, content):
        self.set_content(content)

    def set_content(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

    def stringify(self):
        return self.__content


class CallExp(Stmt, Namiable):
    def __init__(self, name, arguments=[]):
        self.set_name(name)
        self.__arguments = arguments

    def stringify(self):
        return '' + self.get_name() + '(' + \
            (', '.join([a.stringify() for a in self.__arguments])) \
            + ')'


class Action(CallExp):
    pass


class Target(CallExp):
    pass


class BuildFile(Stringify):
    def __init__(self, stat_s=[]):
        self.__stat_s = stat_s

    def append(self, stat):
        self.__stat_s.append(stat)

    def __getitem__(self, key):
        pass

    def stringify(self):
        return '\n'.join([s.stringify() for s in self.__stat_s])


class _MyVisitor(BazelBuildVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        stat_s = [self.visit(stat) for stat in ctx.stat()]
        return BuildFile(stat_s=stat_s)

    # Visit a parse tree produced by BazelBuildParser#callExp.
    def visitCallExp(self, ctx):
        name = ctx.NAME().getText()
        arguments = self.visit(ctx.arg_list())
        return CallExp(name, arguments=arguments)

    # Visit a parse tree produced by BazelBuildParser#arg_list.
    def visitArg_list(self, ctx):
        return [self.visit(argument) for argument in ctx.argument()]

    # Visit a parse tree produced by BazelBuildParser#singleValue.
    def visitSingleValue(self, ctx):
        s = ctx.STRING_VALUE().getText() if ctx.STRING_VALUE() else ''
        return Argument(isMulti=False, values=[s])

    # Visit a parse tree produced by BazelBuildParser#multiValue.

    def visitMultiValue(self, ctx):
        return Argument(isMulti=True, values=self.visit(ctx.val_list()))

    # Visit a parse tree produced by BazelBuildParser#val_list.

    def visitVal_list(self, ctx):
        return [tk.getText() for tk in ctx.STRING_VALUE()]

    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx):
        name = ctx.NAME().getText() if ctx.NAME() else ''
        arg = self.visit(ctx.value())
        arg.set_name(name)
        return arg

    # Visit a parse tree produced by BazelBuildParser#noteExp.
    def visitNoteExp(self, ctx):
        return NoteExp(ctx.LONG_STRING().getText())


class BazelFileFactory:
    @staticmethod
    def createFromString(content):
        stream = antlr.InputStream(content)
        lexer = BazelBuildLexer(stream)
        token_stream = antlr.CommonTokenStream(lexer)
        parser = BazelBuildParser(token_stream)
        tree = parser.prog()
        visitor = _MyVisitor()
        return visitor.visit(tree)

    @staticmethod
    def createFromFile(BUILD_file_path):
        with open(BUILD_file_path, 'r') as f:
            return BazelFileFactory.createFromString(f.read().strip())
        return None


class DefaultDeleter(Deleter):
    def __init__(self, build_file):
        self.__build_file = build_file

    def deep_remove_target(self, name):
        pass
