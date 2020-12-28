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


    # Visit a parse tree produced by BazelBuildParser#target_exp.
    def visitTarget_exp(self, ctx:BazelBuildParser.Target_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#attr_list.
    def visitAttr_list(self, ctx:BazelBuildParser.Attr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#assign_exp.
    def visitAssign_exp(self, ctx:BazelBuildParser.Assign_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#value_exp.
    def visitValue_exp(self, ctx:BazelBuildParser.Value_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#key_word.
    def visitKey_word(self, ctx:BazelBuildParser.Key_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#arglist.
    def visitArglist(self, ctx:BazelBuildParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx:BazelBuildParser.ArgumentContext):
        return self.visitChildren(ctx)



del BazelBuildParser