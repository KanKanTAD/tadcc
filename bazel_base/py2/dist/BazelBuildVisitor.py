# Generated from ./BazelBuild.g4 by ANTLR 4.9
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by BazelBuildParser.

class BazelBuildVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#arg_list.
    def visitArg_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#value.
    def visitValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#val_list.
    def visitVal_list(self, ctx):
        return self.visitChildren(ctx)


