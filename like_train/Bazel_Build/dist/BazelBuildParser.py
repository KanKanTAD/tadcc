# Generated from BazelBuild.y by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\20F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3")
        buf.write(u"\3\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6.\n\6\3\7\3\7\3\7\3\7")
        buf.write(u"\3\b\3\b\5\b\66\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t>\n\t")
        buf.write(u"\3\n\3\n\3\n\3\n\5\nD\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20")
        buf.write(u"\22\2\2\2C\2\25\3\2\2\2\4\34\3\2\2\2\6\36\3\2\2\2\b#")
        buf.write(u"\3\2\2\2\n-\3\2\2\2\f/\3\2\2\2\16\65\3\2\2\2\20=\3\2")
        buf.write(u"\2\2\22C\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3")
        buf.write(u"\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\35")
        buf.write(u"\5\6\4\2\32\35\5\b\5\2\33\35\7\t\2\2\34\31\3\2\2\2\34")
        buf.write(u"\32\3\2\2\2\34\33\3\2\2\2\35\5\3\2\2\2\36\37\7\20\2\2")
        buf.write(u"\37 \7\f\2\2 !\5\22\n\2!\"\7\r\2\2\"\7\3\2\2\2#$\7\5")
        buf.write(u"\2\2$%\7\f\2\2%&\5\n\6\2&\'\7\r\2\2\'\t\3\2\2\2(.\5\f")
        buf.write(u"\7\2)*\5\f\7\2*+\7\3\2\2+,\5\n\6\2,.\3\2\2\2-(\3\2\2")
        buf.write(u"\2-)\3\2\2\2.\13\3\2\2\2/\60\7\5\2\2\60\61\7\4\2\2\61")
        buf.write(u"\62\5\16\b\2\62\r\3\2\2\2\63\66\7\b\2\2\64\66\5\20\t")
        buf.write(u"\2\65\63\3\2\2\2\65\64\3\2\2\2\66\17\3\2\2\2\678\7\16")
        buf.write(u"\2\28>\7\17\2\29:\7\16\2\2:;\5\22\n\2;<\7\17\2\2<>\3")
        buf.write(u"\2\2\2=\67\3\2\2\2=9\3\2\2\2>\21\3\2\2\2?D\7\b\2\2@A")
        buf.write(u"\7\b\2\2AB\7\3\2\2BD\5\22\n\2C?\3\2\2\2C@\3\2\2\2D\23")
        buf.write(u"\3\2\2\2\b\27\34-\65=C")
        return buf.getvalue()


class BazelBuildParser ( Parser ):

    grammarFileName = "BazelBuild.y"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'='", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'('", u"')'", u"'['", u"']'", u"'load'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"Symbol", 
                      u"Comment", u"WS", u"ShortString", u"LongString", 
                      u"LongStringItem", u"RN", u"OpenParen", u"CloseParen", 
                      u"OpenBracket", u"CloseBracket", u"Load" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_load_exp = 2
    RULE_target_exp = 3
    RULE_assign_items = 4
    RULE_assign_exp = 5
    RULE_value_exp = 6
    RULE_list_exp = 7
    RULE_str_items = 8

    ruleNames =  [ u"prog", u"stat", u"load_exp", u"target_exp", u"assign_items", 
                   u"assign_exp", u"value_exp", u"list_exp", u"str_items" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Symbol=3
    Comment=4
    WS=5
    ShortString=6
    LongString=7
    LongStringItem=8
    RN=9
    OpenParen=10
    CloseParen=11
    OpenBracket=12
    CloseBracket=13
    Load=14

    def __init__(self, input, output=sys.stdout):
        super(BazelBuildParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

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
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.Symbol) | (1 << BazelBuildParser.LongString) | (1 << BazelBuildParser.Load))) != 0)):
                    break

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

        def load_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Load_expContext,0)


        def target_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Target_expContext,0)


        def LongString(self):
            return self.getToken(BazelBuildParser.LongString, 0)

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
            if token in [BazelBuildParser.Load]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.load_exp()
                pass
            elif token in [BazelBuildParser.Symbol]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.target_exp()
                pass
            elif token in [BazelBuildParser.LongString]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(BazelBuildParser.LongString)
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

    class Load_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Load_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Load(self):
            return self.getToken(BazelBuildParser.Load, 0)

        def OpenParen(self):
            return self.getToken(BazelBuildParser.OpenParen, 0)

        def str_items(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_itemsContext,0)


        def CloseParen(self):
            return self.getToken(BazelBuildParser.CloseParen, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_load_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterLoad_exp"):
                listener.enterLoad_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLoad_exp"):
                listener.exitLoad_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLoad_exp"):
                return visitor.visitLoad_exp(self)
            else:
                return visitor.visitChildren(self)




    def load_exp(self):

        localctx = BazelBuildParser.Load_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_load_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(BazelBuildParser.Load)
            self.state = 29
            self.match(BazelBuildParser.OpenParen)
            self.state = 30
            self.str_items()
            self.state = 31
            self.match(BazelBuildParser.CloseParen)
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

        def Symbol(self):
            return self.getToken(BazelBuildParser.Symbol, 0)

        def OpenParen(self):
            return self.getToken(BazelBuildParser.OpenParen, 0)

        def assign_items(self):
            return self.getTypedRuleContext(BazelBuildParser.Assign_itemsContext,0)


        def CloseParen(self):
            return self.getToken(BazelBuildParser.CloseParen, 0)

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
            self.state = 33
            self.match(BazelBuildParser.Symbol)
            self.state = 34
            self.match(BazelBuildParser.OpenParen)
            self.state = 35
            self.assign_items()
            self.state = 36
            self.match(BazelBuildParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Assign_itemsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assign_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Assign_expContext,0)


        def assign_items(self):
            return self.getTypedRuleContext(BazelBuildParser.Assign_itemsContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_assign_items

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_items"):
                listener.enterAssign_items(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_items"):
                listener.exitAssign_items(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign_items"):
                return visitor.visitAssign_items(self)
            else:
                return visitor.visitChildren(self)




    def assign_items(self):

        localctx = BazelBuildParser.Assign_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_items)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.assign_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.assign_exp()
                self.state = 40
                self.match(BazelBuildParser.T__0)
                self.state = 41
                self.assign_items()
                pass


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
            self.left = None # Token
            self.right = None # Value_expContext

        def Symbol(self):
            return self.getToken(BazelBuildParser.Symbol, 0)

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
            self.state = 45
            localctx.left = self.match(BazelBuildParser.Symbol)
            self.state = 46
            self.match(BazelBuildParser.T__1)
            self.state = 47
            localctx.right = self.value_exp()
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

        def ShortString(self):
            return self.getToken(BazelBuildParser.ShortString, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.List_expContext,0)


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
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.ShortString]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(BazelBuildParser.ShortString)
                pass
            elif token in [BazelBuildParser.OpenBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.list_exp()
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

    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.List_expContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OpenBracket(self):
            return self.getToken(BazelBuildParser.OpenBracket, 0)

        def CloseBracket(self):
            return self.getToken(BazelBuildParser.CloseBracket, 0)

        def str_items(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_itemsContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_list_exp

        def enterRule(self, listener):
            if hasattr(listener, "enterList_exp"):
                listener.enterList_exp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_exp"):
                listener.exitList_exp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitList_exp"):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = BazelBuildParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_exp)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(BazelBuildParser.OpenBracket)
                self.state = 54
                self.match(BazelBuildParser.CloseBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(BazelBuildParser.OpenBracket)
                self.state = 56
                self.str_items()
                self.state = 57
                self.match(BazelBuildParser.CloseBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Str_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Str_itemsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ShortString(self):
            return self.getToken(BazelBuildParser.ShortString, 0)

        def str_items(self):
            return self.getTypedRuleContext(BazelBuildParser.Str_itemsContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_str_items

        def enterRule(self, listener):
            if hasattr(listener, "enterStr_items"):
                listener.enterStr_items(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStr_items"):
                listener.exitStr_items(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStr_items"):
                return visitor.visitStr_items(self)
            else:
                return visitor.visitChildren(self)




    def str_items(self):

        localctx = BazelBuildParser.Str_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_str_items)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(BazelBuildParser.ShortString)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(BazelBuildParser.ShortString)
                self.state = 63
                self.match(BazelBuildParser.T__0)
                self.state = 64
                self.str_items()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





