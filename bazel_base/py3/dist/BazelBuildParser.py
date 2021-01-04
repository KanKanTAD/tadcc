# Generated from BazelBuild.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4")
        buf.write("\3\4\7\4(\n\4\f\4\16\4+\13\4\3\4\5\4.\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\5\6\67\n\6\3\7\3\7\5\7;\n\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\7\bB\n\b\f\b\16\bE\13\b\3\b\5\bH\n\b\3\t\3")
        buf.write("\t\3\t\5!)C\2\n\2\4\6\b\n\f\16\20\2\2\2L\2\25\3\2\2\2")
        buf.write("\4\30\3\2\2\2\6$\3\2\2\2\b/\3\2\2\2\n\66\3\2\2\2\f8\3")
        buf.write("\2\2\2\16>\3\2\2\2\20I\3\2\2\2\22\24\5\4\3\2\23\22\3\2")
        buf.write("\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3")
        buf.write("\2\2\2\27\25\3\2\2\2\30\31\7\t\2\2\31\33\7\3\2\2\32\34")
        buf.write("\5\6\4\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("!\7\4\2\2\36 \7\f\2\2\37\36\3\2\2\2 #\3\2\2\2!\"\3\2\2")
        buf.write("\2!\37\3\2\2\2\"\5\3\2\2\2#!\3\2\2\2$)\5\b\5\2%&\7\5\2")
        buf.write("\2&(\5\b\5\2\'%\3\2\2\2(+\3\2\2\2)*\3\2\2\2)\'\3\2\2\2")
        buf.write("*-\3\2\2\2+)\3\2\2\2,.\7\5\2\2-,\3\2\2\2-.\3\2\2\2.\7")
        buf.write("\3\2\2\2/\60\7\t\2\2\60\61\7\6\2\2\61\62\3\2\2\2\62\63")
        buf.write("\5\n\6\2\63\t\3\2\2\2\64\67\5\20\t\2\65\67\5\f\7\2\66")
        buf.write("\64\3\2\2\2\66\65\3\2\2\2\67\13\3\2\2\28:\7\7\2\29;\5")
        buf.write("\16\b\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\7\b\2\2=\r\3\2")
        buf.write("\2\2>C\5\20\t\2?@\7\5\2\2@B\5\20\t\2A?\3\2\2\2BE\3\2\2")
        buf.write("\2CD\3\2\2\2CA\3\2\2\2DG\3\2\2\2EC\3\2\2\2FH\7\5\2\2G")
        buf.write("F\3\2\2\2GH\3\2\2\2H\17\3\2\2\2IJ\7\n\2\2J\21\3\2\2\2")
        buf.write("\13\25\33!)-\66:CG")
        return buf.getvalue()


class BazelBuildParser ( Parser ):

    grammarFileName = "BazelBuild.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'='", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "StringValue", 
                      "Whitespace", "Newline", "BlockComment", "LineComment" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_arglist = 2
    RULE_argument = 3
    RULE_value = 4
    RULE_multi_value = 5
    RULE_val_list = 6
    RULE_single_value = 7

    ruleNames =  [ "prog", "stat", "arglist", "argument", "value", "multi_value", 
                   "val_list", "single_value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    StringValue=8
    Whitespace=9
    Newline=10
    BlockComment=11
    LineComment=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.StatContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.StatContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = BazelBuildParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BazelBuildParser.ID:
                self.state = 16
                self.stat()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BazelBuildParser.ID, 0)

        def arglist(self):
            return self.getTypedRuleContext(BazelBuildParser.ArglistContext,0)


        def Newline(self, i:int=None):
            if i is None:
                return self.getTokens(BazelBuildParser.Newline)
            else:
                return self.getToken(BazelBuildParser.Newline, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = BazelBuildParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(BazelBuildParser.ID)
            self.state = 23
            self.match(BazelBuildParser.T__0)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.ID:
                self.state = 24
                self.arglist()


            self.state = 27
            self.match(BazelBuildParser.T__1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 28
                    self.match(BazelBuildParser.Newline) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.ArgumentContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = BazelBuildParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.argument()
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 35
                    self.match(BazelBuildParser.T__2)
                    self.state = 36
                    self.argument() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 42
                self.match(BazelBuildParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(BazelBuildParser.ValueContext,0)


        def ID(self):
            return self.getToken(BazelBuildParser.ID, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = BazelBuildParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(BazelBuildParser.ID)
            self.state = 46
            self.match(BazelBuildParser.T__3)
            self.state = 48
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazelBuildParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleVContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazelBuildParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def single_value(self):
            return self.getTypedRuleContext(BazelBuildParser.Single_valueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleV" ):
                listener.enterSingleV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleV" ):
                listener.exitSingleV(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleV" ):
                return visitor.visitSingleV(self)
            else:
                return visitor.visitChildren(self)


    class MultiVContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazelBuildParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multi_value(self):
            return self.getTypedRuleContext(BazelBuildParser.Multi_valueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiV" ):
                listener.enterMultiV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiV" ):
                listener.exitMultiV(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiV" ):
                return visitor.visitMultiV(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = BazelBuildParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.StringValue]:
                localctx = BazelBuildParser.SingleVContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.single_value()
                pass
            elif token in [BazelBuildParser.T__4]:
                localctx = BazelBuildParser.MultiVContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.multi_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Val_listContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_multi_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_value" ):
                listener.enterMulti_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_value" ):
                listener.exitMulti_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_value" ):
                return visitor.visitMulti_value(self)
            else:
                return visitor.visitChildren(self)




    def multi_value(self):

        localctx = BazelBuildParser.Multi_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multi_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(BazelBuildParser.T__4)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.StringValue:
                self.state = 55
                self.val_list()


            self.state = 58
            self.match(BazelBuildParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.Single_valueContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.Single_valueContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_val_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal_list" ):
                listener.enterVal_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal_list" ):
                listener.exitVal_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_list" ):
                return visitor.visitVal_list(self)
            else:
                return visitor.visitChildren(self)




    def val_list(self):

        localctx = BazelBuildParser.Val_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_val_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.single_value()
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 61
                    self.match(BazelBuildParser.T__2)
                    self.state = 62
                    self.single_value() 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 68
                self.match(BazelBuildParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringValue(self):
            return self.getToken(BazelBuildParser.StringValue, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_single_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_value" ):
                listener.enterSingle_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_value" ):
                listener.exitSingle_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_value" ):
                return visitor.visitSingle_value(self)
            else:
                return visitor.visitChildren(self)




    def single_value(self):

        localctx = BazelBuildParser.Single_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_single_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BazelBuildParser.StringValue)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





