# Generated from ./BazelBuild.g4 by ANTLR 4.9
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\17I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write(u"\5\3\32\n\3\3\3\3\3\5\3\36\n\3\3\3\3\3\5\3\"\n\3\5\3")
        buf.write(u"$\n\3\3\4\3\4\3\4\7\4)\n\4\f\4\16\4,\13\4\3\4\5\4/\n")
        buf.write(u"\4\3\5\3\5\5\5\63\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write(u"<\n\6\3\7\3\7\3\7\7\7A\n\7\f\7\16\7D\13\7\3\7\5\7G\n")
        buf.write(u"\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2M\2\21\3\2\2\2\4#\3\2\2")
        buf.write(u"\2\6%\3\2\2\2\b\62\3\2\2\2\n;\3\2\2\2\f=\3\2\2\2\16\20")
        buf.write(u"\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21")
        buf.write(u"\22\3\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\25\7\2\2\3")
        buf.write(u"\25\3\3\2\2\2\26\27\7\t\2\2\27\31\7\3\2\2\30\32\5\6\4")
        buf.write(u"\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\35\7")
        buf.write(u"\4\2\2\34\36\7\r\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36$")
        buf.write(u"\3\2\2\2\37!\7\13\2\2 \"\7\r\2\2! \3\2\2\2!\"\3\2\2\2")
        buf.write(u"\"$\3\2\2\2#\26\3\2\2\2#\37\3\2\2\2$\5\3\2\2\2%*\5\b")
        buf.write(u"\5\2&\'\7\5\2\2\')\5\b\5\2(&\3\2\2\2),\3\2\2\2*(\3\2")
        buf.write(u"\2\2*+\3\2\2\2+.\3\2\2\2,*\3\2\2\2-/\7\5\2\2.-\3\2\2")
        buf.write(u"\2./\3\2\2\2/\7\3\2\2\2\60\61\7\t\2\2\61\63\7\6\2\2\62")
        buf.write(u"\60\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\65\5\n\6\2")
        buf.write(u"\65\t\3\2\2\2\66<\7\n\2\2\678\7\7\2\289\5\f\7\29:\7\b")
        buf.write(u"\2\2:<\3\2\2\2;\66\3\2\2\2;\67\3\2\2\2<\13\3\2\2\2=B")
        buf.write(u"\7\n\2\2>?\7\5\2\2?A\7\n\2\2@>\3\2\2\2AD\3\2\2\2B@\3")
        buf.write(u"\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2EG\7\5\2\2FE\3\2")
        buf.write(u"\2\2FG\3\2\2\2G\r\3\2\2\2\r\21\31\35!#*.\62;BF")
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
                      u"STRING_VALUE", u"LONG_STRING", u"LONG_STRING_ITEM", 
                      u"RN", u"WS", u"CMT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_arg_list = 2
    RULE_argument = 3
    RULE_value = 4
    RULE_val_list = 5

    ruleNames =  [ u"prog", u"stat", u"arg_list", u"argument", u"value", 
                   u"val_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NAME=7
    STRING_VALUE=8
    LONG_STRING=9
    LONG_STRING_ITEM=10
    RN=11
    WS=12
    CMT=13

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BazelBuildParser.NAME or _la==BazelBuildParser.LONG_STRING:
                self.state = 12
                self.stat()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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


        def getRuleIndex(self):
            return BazelBuildParser.RULE_stat

     
        def copyFrom(self, ctx):
            super(BazelBuildParser.StatContext, self).copyFrom(ctx)



    class NoteExpContext(StatContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.StatContext)
            super(BazelBuildParser.NoteExpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LONG_STRING(self):
            return self.getToken(BazelBuildParser.LONG_STRING, 0)
        def RN(self):
            return self.getToken(BazelBuildParser.RN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterNoteExp"):
                listener.enterNoteExp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNoteExp"):
                listener.exitNoteExp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNoteExp"):
                return visitor.visitNoteExp(self)
            else:
                return visitor.visitChildren(self)


    class CallExpContext(StatContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.StatContext)
            super(BazelBuildParser.CallExpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)
        def arg_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Arg_listContext,0)

        def RN(self):
            return self.getToken(BazelBuildParser.RN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCallExp"):
                listener.enterCallExp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallExp"):
                listener.exitCallExp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCallExp"):
                return visitor.visitCallExp(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = BazelBuildParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.NAME]:
                localctx = BazelBuildParser.CallExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(BazelBuildParser.NAME)
                self.state = 21
                self.match(BazelBuildParser.T__0)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.T__4) | (1 << BazelBuildParser.NAME) | (1 << BazelBuildParser.STRING_VALUE))) != 0):
                    self.state = 22
                    self.arg_list()


                self.state = 25
                self.match(BazelBuildParser.T__1)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.RN:
                    self.state = 26
                    self.match(BazelBuildParser.RN)


                pass
            elif token in [BazelBuildParser.LONG_STRING]:
                localctx = BazelBuildParser.NoteExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(BazelBuildParser.LONG_STRING)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.RN:
                    self.state = 30
                    self.match(BazelBuildParser.RN)


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


    class Arg_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Arg_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.ArgumentContext,i)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_arg_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArg_list"):
                listener.enterArg_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArg_list"):
                listener.exitArg_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArg_list"):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = BazelBuildParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.argument()
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.match(BazelBuildParser.T__2)
                    self.state = 37
                    self.argument() 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 43
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

        def value(self):
            return self.getTypedRuleContext(BazelBuildParser.ValueContext,0)


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
        self.enterRule(localctx, 6, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.NAME:
                self.state = 46
                self.match(BazelBuildParser.NAME)
                self.state = 47
                self.match(BazelBuildParser.T__3)


            self.state = 50
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.ValueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazelBuildParser.RULE_value

     
        def copyFrom(self, ctx):
            super(BazelBuildParser.ValueContext, self).copyFrom(ctx)



    class SingleValueContext(ValueContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.ValueContext)
            super(BazelBuildParser.SingleValueContext, self).__init__(parser)
            self.copyFrom(ctx)

        def STRING_VALUE(self):
            return self.getToken(BazelBuildParser.STRING_VALUE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterSingleValue"):
                listener.enterSingleValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleValue"):
                listener.exitSingleValue(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSingleValue"):
                return visitor.visitSingleValue(self)
            else:
                return visitor.visitChildren(self)


    class MultiValueContext(ValueContext):

        def __init__(self, parser, ctx): # actually a BazelBuildParser.ValueContext)
            super(BazelBuildParser.MultiValueContext, self).__init__(parser)
            self.copyFrom(ctx)

        def val_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Val_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMultiValue"):
                listener.enterMultiValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiValue"):
                listener.exitMultiValue(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMultiValue"):
                return visitor.visitMultiValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = BazelBuildParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.STRING_VALUE]:
                localctx = BazelBuildParser.SingleValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(BazelBuildParser.STRING_VALUE)
                pass
            elif token in [BazelBuildParser.T__4]:
                localctx = BazelBuildParser.MultiValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(BazelBuildParser.T__4)
                self.state = 54
                self.val_list()
                self.state = 55
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


    class Val_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BazelBuildParser.Val_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING_VALUE(self, i=None):
            if i is None:
                return self.getTokens(BazelBuildParser.STRING_VALUE)
            else:
                return self.getToken(BazelBuildParser.STRING_VALUE, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_val_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVal_list"):
                listener.enterVal_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVal_list"):
                listener.exitVal_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitVal_list"):
                return visitor.visitVal_list(self)
            else:
                return visitor.visitChildren(self)




    def val_list(self):

        localctx = BazelBuildParser.Val_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_val_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(BazelBuildParser.STRING_VALUE)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.match(BazelBuildParser.T__2)
                    self.state = 61
                    self.match(BazelBuildParser.STRING_VALUE) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.T__2:
                self.state = 67
                self.match(BazelBuildParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





