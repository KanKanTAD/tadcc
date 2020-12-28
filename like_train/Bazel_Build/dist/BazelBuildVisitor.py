# Generated from BazelBuild.y by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by BazelBuildParser.

class BazelBuildVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#load_exp.
    def visitLoad_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#target_exp.
    def visitTarget_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#assign_items.
    def visitAssign_items(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#assign_exp.
    def visitAssign_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#value_exp.
    def visitValue_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#list_exp.
    def visitList_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#str_items.
    def visitStr_items(self, ctx):
        return self.visitChildren(ctx)


