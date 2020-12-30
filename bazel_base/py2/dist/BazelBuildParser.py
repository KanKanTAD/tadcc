# Generated from ./BazelBuild.g4 by ANTLR 4.9
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\16P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2")
        buf.write(u"\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\5\3\5")
        buf.write(u"\3\5\5\5(\n\5\3\5\3\5\3\6\3\6\3\6\7\6/\n\6\f\6\16\6\62")
        buf.write(u"\13\6\3\6\5\6\65\n\6\3\7\3\7\5\79\n\7\3\7\3\7\3\b\3\b")
        buf.write(u"\3\b\3\b\5\bA\n\b\5\bC\n\b\3\b\5\bF\n\b\3\t\3\t\3\t\7")
        buf.write(u"\tK\n\t\f\t\16\tN\13\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2")
        buf.write(u"\2\2Q\2\25\3\2\2\2\4 \3\2\2\2\6\"\3\2\2\2\b$\3\2\2\2")
        buf.write(u"\n+\3\2\2\2\f8\3\2\2\2\16E\3\2\2\2\20G\3\2\2\2\22\24")
        buf.write(u"\5\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25")
        buf.write(u"\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3")
        buf.write(u"\31\3\3\2\2\2\32\33\5\b\5\2\33\34\7\n\2\2\34!\3\2\2\2")
        buf.write(u"\35\36\5\6\4\2\36\37\7\n\2\2\37!\3\2\2\2 \32\3\2\2\2")
        buf.write(u" \35\3\2\2\2!\5\3\2\2\2\"#\7\r\2\2#\7\3\2\2\2$%\7\t\2")
        buf.write(u"\2%\'\7\3\2\2&(\5\n\6\2\'&\3\2\2\2\'(\3\2\2\2()\3\2\2")
        buf.write(u"\2)*\7\4\2\2*\t\3\2\2\2+\60\5\f\7\2,-\7\5\2\2-/\5\f\7")
        buf.write(u"\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write(u"\64\3\2\2\2\62\60\3\2\2\2\63\65\7\5\2\2\64\63\3\2\2\2")
        buf.write(u"\64\65\3\2\2\2\65\13\3\2\2\2\66\67\7\t\2\2\679\7\6\2")
        buf.write(u"\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:;\5\16\b\2;\r\3\2")
        buf.write(u"\2\2<F\7\r\2\2=B\7\7\2\2>@\5\20\t\2?A\7\5\2\2@?\3\2\2")
        buf.write(u"\2@A\3\2\2\2AC\3\2\2\2B>\3\2\2\2BC\3\2\2\2CD\3\2\2\2")
        buf.write(u"DF\7\b\2\2E<\3\2\2\2E=\3\2\2\2F\17\3\2\2\2GL\7\r\2\2")
        buf.write(u"HI\7\5\2\2IK\7\r\2\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM")
        buf.write(u"\3\2\2\2M\21\3\2\2\2NL\3\2\2\2\f\25 \'\60\648@BEL")
        return buf.getvalue()


class BazelBuildParser ( Parser ):

    grammarFileName = "BazelBuild.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"','", u"'='", u"'['", 
                     u"']'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"NAME", 
                      u"NEWLINE", u"SP", u"CMT", u"STRING", u"KEY_WORD" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_single_exp = 2
    RULE_call_exp = 3
    RULE_argument_list = 4
    RULE_argument = 5
    RULE_value_exp = 6
    RULE_str_list = 7

    ruleNames =  [ u"prog", u"stat", u"single_exp", u"call_exp", u"argument_list", 
                   u"argument", u"value_exp", u"str_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NAME=7
    NEWLINE=8
    SP=9
    CMT=10
    STRING=11
    KEY_WORD=12

    def __init__(self, input, output=sys.stdout):
        super(BazelBuildParser, self).__init__(input, output=output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BazelBuildParser.EOF, 0)

        def stat(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.StatContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.StatContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_prog

        def enterRule(self, listener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
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
            while _la==BazelBuildParser.NAME or _la==BazelBuildParser.STRING:
                self.state = 16
                self.stat()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(BazelBuildParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser

        def call_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Call_expContext,0)


        def NEWLINE(self):
            return self.getToken(BazelBuildParser.NEWLINE, 0)

        def single_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Single_expContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_stat

        def enterRule(self, listener):
            if hasattr(listener, "enterStat"):
                listener.enterStat(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStat"):
                listener.exitStat(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStat"):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = BazelBuildParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.call_exp()
                self.state = 25
                self.match(BazelBuildParser.NEWLINE)
                pass
            elif token in [BazelBuildParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.single_exp()
                self.state = 28
                self.match(BazelBuildParser.NEWLINE)
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


    class Single_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Single_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BazelBuildParser.STRING, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_single_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterSingle_exp"):
                listener.enterSingle_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingle_exp"):
                listener.exitSingle_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSingle_exp"):
                return visitor.visitSingle_exp(self)
            else:
                return visitor.visitChildren(self)




    def single_exp(self):

        localctx = BazelBuildParser.Single_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_single_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(BazelBuildParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Call_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_call_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterCall_exp"):
                listener.enterCall_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCall_exp"):
                listener.exitCall_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCall_exp"):
                return visitor.visitCall_exp(self)
            else:
                return visitor.visitChildren(self)




    def call_exp(self):

        localctx = BazelBuildParser.Call_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(BazelBuildParser.NAME)
            self.state = 35
            self.match(BazelBuildParser.T__0)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.T__4) | (1 << BazelBuildParser.NAME) | (1 << BazelBuildParser.STRING))) != 0):
                self.state = 36
                self.argument_list()


            self.state = 39
            self.match(BazelBuildParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.ArgumentContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArgument_list"):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = BazelBuildParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.argument()
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.match(BazelBuildParser.T__2)
                    self.state = 43
                    self.argument() 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 49
                self.match(BazelBuildParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Value_expContext,0)


        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArgument"):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = BazelBuildParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.NAME:
                self.state = 52
                self.match(BazelBuildParser.NAME)
                self.state = 53
                self.match(BazelBuildParser.T__3)


            self.state = 56
            self.value_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Value_expContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazelBuildParser.RULE_value_exp

     
        def copyFrom(self, ctx):
            super(BazelBuildParser.Value_expContext, self).copyFrom(ctx)



    class Signle_valueContext(Value_expContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.Value_expContext)
            super(BazelBuildParser.Signle_valueContext, self).__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BazelBuildParser.STRING, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterSignle_value"):
                listener.enterSignle_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSignle_value"):
                listener.exitSignle_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSignle_value"):
                return visitor.visitSignle_value(self)
            else:
                return visitor.visitChildren(self)


    class Multi_valueContext(Value_expContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.Value_expContext)
            super(BazelBuildParser.Multi_valueContext, self).__init__(parser)
            self.copyFrom(ctx)

        def str_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMulti_value"):
                listener.enterMulti_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMulti_value"):
                listener.exitMulti_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMulti_value"):
                return visitor.visitMulti_value(self)
            else:
                return visitor.visitChildren(self)



    def value_exp(self):

        localctx = BazelBuildParser.Value_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value_exp)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.STRING]:
                localctx = BazelBuildParser.Signle_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(BazelBuildParser.STRING)
                pass
            elif token in [BazelBuildParser.T__4]:
                localctx = BazelBuildParser.Multi_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(BazelBuildParser.T__4)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.STRING:
                    self.state = 60
                    self.str_list()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BazelBuildParser.T__2:
                        self.state = 61
                        self.match(BazelBuildParser.T__2)




                self.state = 66
                self.match(BazelBuildParser.T__5)
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


    class Str_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Str_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i=None):
            if i is None:
                return self.getTokens(BazelBuildParser.STRING)
            else:
                return self.getToken(BazelBuildParser.STRING, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_str_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStr_list"):
                listener.enterStr_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStr_list"):
                listener.exitStr_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStr_list"):
                return visitor.visitStr_list(self)
            else:
                return visitor.visitChildren(self)




    def str_list(self):

        localctx = BazelBuildParser.Str_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_str_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(BazelBuildParser.STRING)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self.match(BazelBuildParser.T__2)
                    self.state = 71
                    self.match(BazelBuildParser.STRING) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





