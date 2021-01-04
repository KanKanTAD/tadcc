# Generated from BazelBuild.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BazelBuildParser import BazelBuildParser
else:
    from BazelBuildParser import BazelBuildParser

# This class defines a complete generic visitor for a parse tree produced by BazelBuildParser.

class BazelBuildVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx:BazelBuildParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#stat.
    def visitStat(self, ctx:BazelBuildParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#arglist.
    def visitArglist(self, ctx:BazelBuildParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx:BazelBuildParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#singleV.
    def visitSingleV(self, ctx:BazelBuildParser.SingleVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#multiV.
    def visitMultiV(self, ctx:BazelBuildParser.MultiVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#multi_value.
    def visitMulti_value(self, ctx:BazelBuildParser.Multi_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#val_list.
    def visitVal_list(self, ctx:BazelBuildParser.Val_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#single_value.
    def visitSingle_value(self, ctx:BazelBuildParser.Single_valueContext):
        return self.visitChildren(ctx)



del BazelBuildParser