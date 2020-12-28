import sys
from antlr4 import *
from dist.CalculantlrLexer import CalculantlrLexer
from dist.CalculantlrParser import CalculantlrParser
from dist.CalculantlrVisitor import CalculantlrVisitor


class CalcVisitor(CalculantlrVisitor):
    def visitAtomExpr(self, ctx):
        return int(ctx.getText())

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r


def calc(line):
    input_stream = InputStream(line)

    # lexing
    lexer = CalculantlrLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculantlrParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    while True:
        print ">>> "
        line = input()
        print(calc(line))
