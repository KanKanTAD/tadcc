# Generated from ./BazelBuild.g4 by ANTLR 4.9
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\16L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2")
        buf.write(u"\3\2\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6.\n\6\f\6\16\6\61")
        buf.write(u"\13\6\3\6\5\6\64\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\5\b?\n\b\3\b\5\bB\n\b\3\t\3\t\3\t\7\tG\n\t\f\t\16")
        buf.write(u"\tJ\13\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2K\2\25\3\2")
        buf.write(u"\2\2\4\34\3\2\2\2\6\36\3\2\2\2\b%\3\2\2\2\n*\3\2\2\2")
        buf.write(u"\f\65\3\2\2\2\16A\3\2\2\2\20C\3\2\2\2\22\24\5\4\3\2\23")
        buf.write(u"\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write(u"\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2")
        buf.write(u"\2\32\35\5\6\4\2\33\35\5\b\5\2\34\32\3\2\2\2\34\33\3")
        buf.write(u"\2\2\2\35\5\3\2\2\2\36\37\7\16\2\2\37!\7\3\2\2 \"\5\20")
        buf.write(u"\t\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7\4\2\2$\7\3\2")
        buf.write(u"\2\2%&\7\t\2\2&\'\7\3\2\2\'(\5\n\6\2()\7\4\2\2)\t\3\2")
        buf.write(u"\2\2*/\5\f\7\2+,\7\5\2\2,.\5\f\7\2-+\3\2\2\2.\61\3\2")
        buf.write(u"\2\2/-\3\2\2\2/\60\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2")
        buf.write(u"\62\64\7\5\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\13\3\2")
        buf.write(u"\2\2\65\66\7\t\2\2\66\67\7\6\2\2\678\5\16\b\28\r\3\2")
        buf.write(u"\2\29B\7\r\2\2:>\7\7\2\2;<\5\20\t\2<=\7\5\2\2=?\3\2\2")
        buf.write(u"\2>;\3\2\2\2>?\3\2\2\2?@\3\2\2\2@B\7\b\2\2A9\3\2\2\2")
        buf.write(u"A:\3\2\2\2B\17\3\2\2\2CH\7\r\2\2DE\7\5\2\2EG\7\r\2\2")
        buf.write(u"FD\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\21\3\2\2\2")
        buf.write(u"JH\3\2\2\2\n\25\34!/\63>AH")
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
    RULE_action_exp = 2
    RULE_target_exp = 3
    RULE_assign_list = 4
    RULE_assign_exp = 5
    RULE_value_exp = 6
    RULE_str_list = 7

    ruleNames =  [ u"prog", u"stat", u"action_exp", u"target_exp", u"assign_list", 
                   u"assign_exp", u"value_exp", u"str_list" ]

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
            while _la==BazelBuildParser.NAME or _la==BazelBuildParser.KEY_WORD:
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

        def action_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Action_expContext,0)


        def target_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Target_expContext,0)


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
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.KEY_WORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.action_exp()
                pass
            elif token in [BazelBuildParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.target_exp()
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


    class Action_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Action_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def KEY_WORD(self):
            return self.getToken(BazelBuildParser.KEY_WORD, 0)

        def str_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_listContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_action_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterAction_exp"):
                listener.enterAction_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAction_exp"):
                listener.exitAction_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAction_exp"):
                return visitor.visitAction_exp(self)
            else:
                return visitor.visitChildren(self)




    def action_exp(self):

        localctx = BazelBuildParser.Action_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_action_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(BazelBuildParser.KEY_WORD)
            self.state = 29
            self.match(BazelBuildParser.T__0)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.STRING:
                self.state = 30
                self.str_list()


            self.state = 33
            self.match(BazelBuildParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Target_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Target_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def assign_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Assign_listContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_target_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterTarget_exp"):
                listener.enterTarget_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTarget_exp"):
                listener.exitTarget_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTarget_exp"):
                return visitor.visitTarget_exp(self)
            else:
                return visitor.visitChildren(self)




    def target_exp(self):

        localctx = BazelBuildParser.Target_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_target_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(BazelBuildParser.NAME)
            self.state = 36
            self.match(BazelBuildParser.T__0)
            self.state = 37
            self.assign_list()
            self.state = 38
            self.match(BazelBuildParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Assign_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assign_exp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.Assign_expContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.Assign_expContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_assign_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_list"):
                listener.enterAssign_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_list"):
                listener.exitAssign_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign_list"):
                return visitor.visitAssign_list(self)
            else:
                return visitor.visitChildren(self)




    def assign_list(self):

        localctx = BazelBuildParser.Assign_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.assign_exp()
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 41
                    self.match(BazelBuildParser.T__2)
                    self.state = 42
                    self.assign_exp() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 48
                self.match(BazelBuildParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Assign_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def value_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Value_expContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_assign_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_exp"):
                listener.enterAssign_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_exp"):
                listener.exitAssign_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign_exp"):
                return visitor.visitAssign_exp(self)
            else:
                return visitor.visitChildren(self)




    def assign_exp(self):

        localctx = BazelBuildParser.Assign_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(BazelBuildParser.NAME)
            self.state = 52
            self.match(BazelBuildParser.T__3)
            self.state = 53
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

        def STRING(self):
            return self.getToken(BazelBuildParser.STRING, 0)

        def str_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_listContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_value_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_exp"):
                listener.enterValue_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_exp"):
                listener.exitValue_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitValue_exp"):
                return visitor.visitValue_exp(self)
            else:
                return visitor.visitChildren(self)




    def value_exp(self):

        localctx = BazelBuildParser.Value_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value_exp)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(BazelBuildParser.STRING)
                pass
            elif token in [BazelBuildParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(BazelBuildParser.T__4)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.STRING:
                    self.state = 57
                    self.str_list()
                    self.state = 58
                    self.match(BazelBuildParser.T__2)


                self.state = 62
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
            self.state = 65
            self.match(BazelBuildParser.STRING)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(BazelBuildParser.T__2)
                    self.state = 67
                    self.match(BazelBuildParser.STRING) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





