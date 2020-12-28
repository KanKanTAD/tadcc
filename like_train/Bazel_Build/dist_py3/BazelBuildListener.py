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


    # Enter a parse tree produced by BazelBuildParser#target_exp.
    def enterTarget_exp(self, ctx:BazelBuildParser.Target_expContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#target_exp.
    def exitTarget_exp(self, ctx:BazelBuildParser.Target_expContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#attr_list.
    def enterAttr_list(self, ctx:BazelBuildParser.Attr_listContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#attr_list.
    def exitAttr_list(self, ctx:BazelBuildParser.Attr_listContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#assign_exp.
    def enterAssign_exp(self, ctx:BazelBuildParser.Assign_expContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#assign_exp.
    def exitAssign_exp(self, ctx:BazelBuildParser.Assign_expContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#value_exp.
    def enterValue_exp(self, ctx:BazelBuildParser.Value_expContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#value_exp.
    def exitValue_exp(self, ctx:BazelBuildParser.Value_expContext):
        pass


    # Enter a parse tree produced by BazelBuildParser#key_word.
    def enterKey_word(self, ctx:BazelBuildParser.Key_wordContext):
        pass

    # Exit a parse tree produced by BazelBuildParser#key_word.
    def exitKey_word(self, ctx:BazelBuildParser.Key_wordContext):
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



del BazelBuildParser