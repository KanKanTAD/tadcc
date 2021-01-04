# Generated from BazelBuild.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BazelBuildParser import BazelBuildParser
else:
    from BazelBuildParser import BazelBuildParser

# This class defines a complete listener for a parse tree produced by BazelBuildParser.
class BazelBuildListener(ParseTreeListener):

    # Enter a parse tree produced by BazelBuildParser#prog.
    def enterProg(self, ctx:BazelBuildParser.ProgContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#prog.
    def exitProg(self, ctx:BazelBuildParser.ProgContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#stat.
    def enterStat(self, ctx:BazelBuildParser.StatContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#stat.
    def exitStat(self, ctx:BazelBuildParser.StatContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#arglist.
    def enterArglist(self, ctx:BazelBuildParser.ArglistContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#arglist.
    def exitArglist(self, ctx:BazelBuildParser.ArglistContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#argument.
    def enterArgument(self, ctx:BazelBuildParser.ArgumentContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#argument.
    def exitArgument(self, ctx:BazelBuildParser.ArgumentContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#singleV.
    def enterSingleV(self, ctx:BazelBuildParser.SingleVContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#singleV.
    def exitSingleV(self, ctx:BazelBuildParser.SingleVContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#multiV.
    def enterMultiV(self, ctx:BazelBuildParser.MultiVContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#multiV.
    def exitMultiV(self, ctx:BazelBuildParser.MultiVContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#multi_value.
    def enterMulti_value(self, ctx:BazelBuildParser.Multi_valueContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#multi_value.
    def exitMulti_value(self, ctx:BazelBuildParser.Multi_valueContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#val_list.
    def enterVal_list(self, ctx:BazelBuildParser.Val_listContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#val_list.
    def exitVal_list(self, ctx:BazelBuildParser.Val_listContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#single_value.
    def enterSingle_value(self, ctx:BazelBuildParser.Single_valueContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#single_value.
    def exitSingle_value(self, ctx:BazelBuildParser.Single_valueContext):
        pass



del BazelBuildParser