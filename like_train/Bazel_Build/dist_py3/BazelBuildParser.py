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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5\5\5\63")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7=\n\7\f\7\16\7")
        buf.write("@\13\7\5\7B\n\7\3\7\3\7\5\7F\n\7\3\b\3\b\3\t\3\t\3\t\7")
        buf.write("\tM\n\t\f\t\16\tP\13\t\5\tR\n\t\3\n\3\n\3\n\2\2\13\2\4")
        buf.write("\6\b\n\f\16\20\22\2\3\3\2\4\b\2V\2\27\3\2\2\2\4#\3\2\2")
        buf.write("\2\6%\3\2\2\2\b\62\3\2\2\2\n\64\3\2\2\2\fE\3\2\2\2\16")
        buf.write("G\3\2\2\2\20Q\3\2\2\2\22S\3\2\2\2\24\26\5\4\3\2\25\24")
        buf.write("\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\32\3\2\2\2\31\27\3\2\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34")
        buf.write("\35\5\16\b\2\35\36\7\r\2\2\36\37\5\20\t\2\37 \7\16\2\2")
        buf.write(" $\3\2\2\2!$\5\6\4\2\"$\7\3\2\2#\34\3\2\2\2#!\3\2\2\2")
        buf.write("#\"\3\2\2\2$\5\3\2\2\2%&\7\n\2\2&\'\7\r\2\2\'(\5\b\5\2")
        buf.write("()\7\16\2\2)\7\3\2\2\2*/\5\n\6\2+,\7\17\2\2,.\5\n\6\2")
        buf.write("-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\63\3\2")
        buf.write("\2\2\61/\3\2\2\2\62*\3\2\2\2\62\63\3\2\2\2\63\t\3\2\2")
        buf.write("\2\64\65\7\n\2\2\65\66\7\20\2\2\66\67\5\f\7\2\67\13\3")
        buf.write("\2\2\28A\7\21\2\29>\7\3\2\2:;\7\17\2\2;=\7\3\2\2<:\3\2")
        buf.write("\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?B\3\2\2\2@>\3\2\2\2")
        buf.write("A9\3\2\2\2AB\3\2\2\2BC\3\2\2\2CF\7\22\2\2DF\7\3\2\2E8")
        buf.write("\3\2\2\2ED\3\2\2\2F\r\3\2\2\2GH\t\2\2\2H\17\3\2\2\2IN")
        buf.write("\5\22\n\2JK\7\17\2\2KM\5\22\n\2LJ\3\2\2\2MP\3\2\2\2NL")
        buf.write("\3\2\2\2NO\3\2\2\2OR\3\2\2\2PN\3\2\2\2QI\3\2\2\2QR\3\2")
        buf.write("\2\2R\21\3\2\2\2ST\7\3\2\2T\23\3\2\2\2\13\27#/\62>AEN")
        buf.write("Q")
        return buf.getvalue()


class BazelBuildParser ( Parser ):

    grammarFileName = "BazelBuild.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'load'", "'exports_files'", 
                     "'workspace'", "'licenses'", "'package_group'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "','", "'='", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "STRING", "LOAD", "EXPORTS", "WORKSPACE", 
                      "LICENSES", "PACKAGE_GROUP", "NEWLINE", "NAME", "STRING_LITERAL", 
                      "BYTES_LITERAL", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", 
                      "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                      "CLOSE_BRACE", "SKIP_", "UNKNOWN_CHAR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_target_exp = 2
    RULE_attr_list = 3
    RULE_assign_exp = 4
    RULE_value_exp = 5
    RULE_key_word = 6
    RULE_arglist = 7
    RULE_argument = 8

    ruleNames =  [ "prog", "stat", "target_exp", "attr_list", "assign_exp", 
                   "value_exp", "key_word", "arglist", "argument" ]

    EOF = Token.EOF
    STRING=1
    LOAD=2
    EXPORTS=3
    WORKSPACE=4
    LICENSES=5
    PACKAGE_GROUP=6
    NEWLINE=7
    NAME=8
    STRING_LITERAL=9
    BYTES_LITERAL=10
    OPEN_PAREN=11
    CLOSE_PAREN=12
    COMMA=13
    ASSIGN=14
    OPEN_BRACK=15
    CLOSE_BRACK=16
    OPEN_BRACE=17
    CLOSE_BRACE=18
    SKIP_=19
    UNKNOWN_CHAR=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BazelBuildParser.EOF, 0)

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BazelBuildParser.STRING) | (1 << BazelBuildParser.LOAD) | (1 << BazelBuildParser.EXPORTS) | (1 << BazelBuildParser.WORKSPACE) | (1 << BazelBuildParser.LICENSES) | (1 << BazelBuildParser.PACKAGE_GROUP) | (1 << BazelBuildParser.NAME))) != 0):
                self.state = 18
                self.stat()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(BazelBuildParser.EOF)
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

        def key_word(self):
            return self.getTypedRuleContext(BazelBuildParser.Key_wordContext,0)


        def OPEN_PAREN(self):
            return self.getToken(BazelBuildParser.OPEN_PAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(BazelBuildParser.ArglistContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(BazelBuildParser.CLOSE_PAREN, 0)

        def target_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Target_expContext,0)


        def STRING(self):
            return self.getToken(BazelBuildParser.STRING, 0)

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
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.LOAD, BazelBuildParser.EXPORTS, BazelBuildParser.WORKSPACE, BazelBuildParser.LICENSES, BazelBuildParser.PACKAGE_GROUP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.key_word()
                self.state = 27
                self.match(BazelBuildParser.OPEN_PAREN)
                self.state = 28
                self.arglist()
                self.state = 29
                self.match(BazelBuildParser.CLOSE_PAREN)
                pass
            elif token in [BazelBuildParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.target_exp()
                pass
            elif token in [BazelBuildParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(BazelBuildParser.STRING)
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


    class Target_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(BazelBuildParser.OPEN_PAREN, 0)

        def attr_list(self):
            return self.getTypedRuleContext(BazelBuildParser.Attr_listContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(BazelBuildParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_target_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget_exp" ):
                listener.enterTarget_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget_exp" ):
                listener.exitTarget_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget_exp" ):
                return visitor.visitTarget_exp(self)
            else:
                return visitor.visitChildren(self)




    def target_exp(self):

        localctx = BazelBuildParser.Target_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_target_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(BazelBuildParser.NAME)
            self.state = 36
            self.match(BazelBuildParser.OPEN_PAREN)
            self.state = 37
            self.attr_list()
            self.state = 38
            self.match(BazelBuildParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.Assign_expContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.Assign_expContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BazelBuildParser.COMMA)
            else:
                return self.getToken(BazelBuildParser.COMMA, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_attr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_list" ):
                listener.enterAttr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_list" ):
                listener.exitAttr_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_list" ):
                return visitor.visitAttr_list(self)
            else:
                return visitor.visitChildren(self)




    def attr_list(self):

        localctx = BazelBuildParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.NAME:
                self.state = 40
                self.assign_exp()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BazelBuildParser.COMMA:
                    self.state = 41
                    self.match(BazelBuildParser.COMMA)
                    self.state = 42
                    self.assign_exp()
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(BazelBuildParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(BazelBuildParser.ASSIGN, 0)

        def value_exp(self):
            return self.getTypedRuleContext(BazelBuildParser.Value_expContext,0)


        def getRuleIndex(self):
            return BazelBuildParser.RULE_assign_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_exp" ):
                listener.enterAssign_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_exp" ):
                listener.exitAssign_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_exp" ):
                return visitor.visitAssign_exp(self)
            else:
                return visitor.visitChildren(self)




    def assign_exp(self):

        localctx = BazelBuildParser.Assign_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(BazelBuildParser.NAME)
            self.state = 51
            self.match(BazelBuildParser.ASSIGN)
            self.state = 52
            self.value_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(BazelBuildParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(BazelBuildParser.CLOSE_BRACK, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(BazelBuildParser.STRING)
            else:
                return self.getToken(BazelBuildParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BazelBuildParser.COMMA)
            else:
                return self.getToken(BazelBuildParser.COMMA, i)

        def getRuleIndex(self):
            return BazelBuildParser.RULE_value_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_exp" ):
                listener.enterValue_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_exp" ):
                listener.exitValue_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_exp" ):
                return visitor.visitValue_exp(self)
            else:
                return visitor.visitChildren(self)




    def value_exp(self):

        localctx = BazelBuildParser.Value_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value_exp)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BazelBuildParser.OPEN_BRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(BazelBuildParser.OPEN_BRACK)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BazelBuildParser.STRING:
                    self.state = 55
                    self.match(BazelBuildParser.STRING)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BazelBuildParser.COMMA:
                        self.state = 56
                        self.match(BazelBuildParser.COMMA)
                        self.state = 57
                        self.match(BazelBuildParser.STRING)
                        self.state = 62
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 65
                self.match(BazelBuildParser.CLOSE_BRACK)
                pass
            elif token in [BazelBuildParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(BazelBuildParser.STRING)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_word" ):
                listener.enterKey_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_word" ):
                listener.exitKey_word(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_word" ):
                return visitor.visitKey_word(self)
            else:
                return visitor.visitChildren(self)




    def key_word(self):

        localctx = BazelBuildParser.Key_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_key_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazelBuildParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(BazelBuildParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BazelBuildParser.COMMA)
            else:
                return self.getToken(BazelBuildParser.COMMA, i)

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
        self.enterRule(localctx, 14, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BazelBuildParser.STRING:
                self.state = 71
                self.argument()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BazelBuildParser.COMMA:
                    self.state = 72
                    self.match(BazelBuildParser.COMMA)
                    self.state = 73
                    self.argument()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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

        def STRING(self):
            return self.getToken(BazelBuildParser.STRING, 0)

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
        self.enterRule(localctx, 16, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(BazelBuildParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





