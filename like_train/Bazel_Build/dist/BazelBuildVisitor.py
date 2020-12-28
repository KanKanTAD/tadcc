# Generated from ./BazelBuild.y by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by BazelBuildParser.

class BazelBuildVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#LoadStat.
    def visitLoadStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#TargetStat.
    def visitTargetStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#LongStrStat.
    def visitLongStrStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#load_exp.
    def visitLoad_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#target_exp.
    def visitTarget_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#SingleAttr.
    def visitSingleAttr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#MultiAttr.
    def visitMultiAttr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#assign_exp.
    def visitAssign_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#SingleValue.
    def visitSingleValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#ListValue.
    def visitListValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#EmptyListValue.
    def visitEmptyListValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#NoEmptyListValue.
    def visitNoEmptyListValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#SingleShortString.
    def visitSingleShortString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#MultiShortString.
    def visitMultiShortString(self, ctx):
        return self.visitChildren(ctx)


