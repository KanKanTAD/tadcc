# Generated from Calculantlr.y by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by CalculantlrParser.

class CalculantlrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculantlrParser#AtomExpr.
    def visitAtomExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#ParenExpr.
    def visitParenExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#OpExpr.
    def visitOpExpr(self, ctx):
        return self.visitChildren(ctx)


