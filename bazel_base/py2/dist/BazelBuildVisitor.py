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


    # Visit a parse tree produced by BazelBuildParser#single_exp.
    def visitSingle_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#call_exp.
    def visitCall_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#argument_list.
    def visitArgument_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#signle_value.
    def visitSignle_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#multi_value.
    def visitMulti_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#str_list.
    def visitStr_list(self, ctx):
        return self.visitChildren(ctx)


