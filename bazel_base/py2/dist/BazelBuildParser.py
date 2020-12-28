# Generated from ./BazelBuild.g4 by ANTLR 4.9
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\21R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4")
        buf.write(u"\3\5\3\5\3\5\7\5*\n\5\f\5\16\5-\13\5\5\5/\n\5\3\6\3\6")
        buf.write(u"\3\6\7\6\64\n\6\f\6\16\6\67\13\6\3\6\5\6:\n\6\3\7\3\7")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b")
        buf.write(u"\3\b\5\bK\n\b\5\bM\n\b\3\b\5\bP\n\b\3\b\2\2\t\2\4\6\b")
        buf.write(u"\n\f\16\2\3\3\2\n\16\2T\2\23\3\2\2\2\4\"\3\2\2\2\6$\3")
        buf.write(u"\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f;\3\2\2\2\16O\3\2\2\2")
        buf.write(u"\20\22\5\4\3\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2")
        buf.write(u"\2\2\23\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27")
        buf.write(u"\7\2\2\3\27\3\3\2\2\2\30\31\5\6\4\2\31\32\7\3\2\2\32")
        buf.write(u"\33\5\b\5\2\33\34\7\4\2\2\34#\3\2\2\2\35\36\7\t\2\2\36")
        buf.write(u"\37\7\3\2\2\37 \5\n\6\2 !\7\4\2\2!#\3\2\2\2\"\30\3\2")
        buf.write(u"\2\2\"\35\3\2\2\2#\5\3\2\2\2$%\t\2\2\2%\7\3\2\2\2&+\7")
        buf.write(u"\21\2\2\'(\7\5\2\2(*\7\21\2\2)\'\3\2\2\2*-\3\2\2\2+)")
        buf.write(u"\3\2\2\2+,\3\2\2\2,/\3\2\2\2-+\3\2\2\2.&\3\2\2\2./\3")
        buf.write(u"\2\2\2/\t\3\2\2\2\60\65\5\f\7\2\61\62\7\5\2\2\62\64\5")
        buf.write(u"\f\7\2\63\61\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write(u"\3\2\2\2\669\3\2\2\2\67\65\3\2\2\28:\7\5\2\298\3\2\2")
        buf.write(u"\29:\3\2\2\2:\13\3\2\2\2;<\7\t\2\2<=\7\6\2\2=>\5\16\b")
        buf.write(u"\2>\r\3\2\2\2?P\7\21\2\2@L\7\7\2\2AF\7\21\2\2BC\7\5\2")
        buf.write(u"\2CE\7\21\2\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write(u"GJ\3\2\2\2HF\3\2\2\2IK\7\5\2\2JI\3\2\2\2JK\3\2\2\2KM")
        buf.write(u"\3\2\2\2LA\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\7\b\2\2O?\3")
        buf.write(u"\2\2\2O@\3\2\2\2P\17\3\2\2\2\f\23\"+.\659FJLO")
        return buf.getvalue()


class BazelBuildParser ( Parser ):

    grammarFileName = "BazelBuild.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"','", u"'='", u"'['", 
                     u"']'", u"<INVALID>", u"'load'", u"'exports_files'", 
                     u"'workspace'", u"'licenses'", u"'package_group'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"NAME", 
                      u"LOAD", u"EXPORTS", u"WORKSPACE", u"LICENSES", u"PACKAGE_GROUP", 
                      u"NEWLINE", u"SP", u"STRING" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_key_word = 2
    RULE_arglist = 3
    RULE_assign_list = 4
    RULE_assign_exp = 5
    RULE_value_exp = 6

    ruleNames =  [ u"prog", u"stat", u"key_word", u"arglist", u"assign_list", 
                   u"assign_exp", u"value_exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NAME=7
    LOAD=8
    EXPORTS=9
    WORKSPACE=10
    LICENSES=11
    PACKAGE_GROUP=12
    NEWLINE=13
    SP=14
    STRING=15

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.NAME) | (1 << BazelBuildParser.LOAD) | (1 << BazelBuildParser.EXPORTS) | (1 << BazelBuildParser.WORKSPACE) | (1 << BazelBuildParser.LICENSES) | (1 << BazelBuildParser.PACKAGE_GROUP))) != 0):
                self.state = 14
                self.stat()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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

        def key_word(self):
            return self.getTypedRuleContext(BazelBuildParser.Key_wordContext,0)


        def arglist(self):
            return self.getTypedRuleContext(BazelBuildParser.ArglistContext,0)


        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def assign_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Assign_listContext,0)


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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.LOAD, BazelBuildParser.EXPORTS, BazelBuildParser.WORKSPACE, BazelBuildParser.LICENSES, BazelBuildParser.PACKAGE_GROUP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.key_word()
                self.state = 23
                self.match(BazelBuildParser.T__0)
                self.state = 24
                self.arglist()
                self.state = 25
                self.match(BazelBuildParser.T__1)
                pass
            elif token in [BazelBuildParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(BazelBuildParser.NAME)
                self.state = 28
                self.match(BazelBuildParser.T__0)
                self.state = 29
                self.assign_list()
                self.state = 30
                self.match(BazelBuildParser.T__1)
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


    class Key_wordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Key_wordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(BazelBuildParser.LOAD, 0)

        def EXPORTS(self):
            return self.getToken(BazelBuildParser.EXPORTS, 0)

        def LICENSES(self):
            return self.getToken(BazelBuildParser.LICENSES, 0)

        def WORKSPACE(self):
            return self.getToken(BazelBuildParser.WORKSPACE, 0)

        def PACKAGE_GROUP(self):
            return self.getToken(BazelBuildParser.PACKAGE_GROUP, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_key_word

        def enterRule(self, listener):
            if hasattr(listener, "enterKey_word"):
                listener.enterKey_word(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_word"):
                listener.exitKey_word(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitKey_word"):
                return visitor.visitKey_word(self)
            else:
                return visitor.visitChildren(self)




    def key_word(self):

        localctx = BazelBuildParser.Key_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.LOAD) | (1 << BazelBuildParser.EXPORTS) | (1 << BazelBuildParser.WORKSPACE) | (1 << BazelBuildParser.LICENSES) | (1 << BazelBuildParser.PACKAGE_GROUP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.ArglistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i=None):
            if i is None:
                return self.getTokens(BazelBuildParser.STRING)
            else:
                return self.getToken(BazelBuildParser.STRING, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_arglist

        def enterRule(self, listener):
            if hasattr(listener, "enterArglist"):
                listener.enterArglist(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArglist"):
                listener.exitArglist(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArglist"):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = BazelBuildParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.STRING:
                self.state = 36
                self.match(BazelBuildParser.STRING)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BazelBuildParser.T__2:
                    self.state = 37
                    self.match(BazelBuildParser.T__2)
                    self.state = 38
                    self.match(BazelBuildParser.STRING)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
            self.state = 46
            self.assign_exp()
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    self.match(BazelBuildParser.T__2)
                    self.state = 48
                    self.assign_exp() 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 54
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
            self.state = 57
            self.match(BazelBuildParser.NAME)
            self.state = 58
            self.match(BazelBuildParser.T__3)
            self.state = 59
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

        def STRING(self, i=None):
            if i is None:
                return self.getTokens(BazelBuildParser.STRING)
            else:
                return self.getToken(BazelBuildParser.STRING, i)

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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(BazelBuildParser.STRING)
                pass
            elif token in [BazelBuildParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(BazelBuildParser.T__4)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.STRING:
                    self.state = 63
                    self.match(BazelBuildParser.STRING)
                    self.state = 68
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 64
                            self.match(BazelBuildParser.T__2)
                            self.state = 65
                            self.match(BazelBuildParser.STRING) 
                        self.state = 70
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BazelBuildParser.T__2:
                        self.state = 71
                        self.match(BazelBuildParser.T__2)




                self.state = 76
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





