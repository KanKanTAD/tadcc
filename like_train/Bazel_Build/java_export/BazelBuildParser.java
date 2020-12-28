// Generated from BazelBuild.y by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BazelBuildParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Symbol=3, Comment=4, WS=5, ShortString=6, LongString=7, 
		LongStringItem=8, RN=9, OpenParen=10, CloseParen=11, OpenBracket=12, CloseBracket=13, 
		Load=14;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_load_exp = 2, RULE_target_exp = 3, 
		RULE_assign_items = 4, RULE_assign_exp = 5, RULE_value_exp = 6, RULE_list_exp = 7, 
		RULE_str_items = 8;
	public static final String[] ruleNames = {
		"prog", "stat", "load_exp", "target_exp", "assign_items", "assign_exp", 
		"value_exp", "list_exp", "str_items"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "','", "'='", null, null, null, null, null, null, null, "'('", "')'", 
		"'['", "']'", "'load'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, "Symbol", "Comment", "WS", "ShortString", "LongString", 
		"LongStringItem", "RN", "OpenParen", "CloseParen", "OpenBracket", "CloseBracket", 
		"Load"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BazelBuild.y"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BazelBuildParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(18);
				stat();
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Symbol) | (1L << LongString) | (1L << Load))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LoadStatContext extends StatContext {
		public Load_expContext load_exp() {
			return getRuleContext(Load_expContext.class,0);
		}
		public LoadStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterLoadStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitLoadStat(this);
		}
	}
	public static class TargetStatContext extends StatContext {
		public Target_expContext target_exp() {
			return getRuleContext(Target_expContext.class,0);
		}
		public TargetStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterTargetStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitTargetStat(this);
		}
	}
	public static class LongStrStatContext extends StatContext {
		public TerminalNode LongString() { return getToken(BazelBuildParser.LongString, 0); }
		public LongStrStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterLongStrStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitLongStrStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(26);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Load:
				_localctx = new LoadStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(23);
				load_exp();
				}
				break;
			case Symbol:
				_localctx = new TargetStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				target_exp();
				}
				break;
			case LongString:
				_localctx = new LongStrStatContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				match(LongString);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Load_expContext extends ParserRuleContext {
		public TerminalNode Load() { return getToken(BazelBuildParser.Load, 0); }
		public TerminalNode OpenParen() { return getToken(BazelBuildParser.OpenParen, 0); }
		public Str_itemsContext str_items() {
			return getRuleContext(Str_itemsContext.class,0);
		}
		public TerminalNode CloseParen() { return getToken(BazelBuildParser.CloseParen, 0); }
		public Load_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_load_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterLoad_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitLoad_exp(this);
		}
	}

	public final Load_expContext load_exp() throws RecognitionException {
		Load_expContext _localctx = new Load_expContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_load_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(Load);
			setState(29);
			match(OpenParen);
			setState(30);
			str_items();
			setState(31);
			match(CloseParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Target_expContext extends ParserRuleContext {
		public TerminalNode Symbol() { return getToken(BazelBuildParser.Symbol, 0); }
		public TerminalNode OpenParen() { return getToken(BazelBuildParser.OpenParen, 0); }
		public Assign_itemsContext assign_items() {
			return getRuleContext(Assign_itemsContext.class,0);
		}
		public TerminalNode CloseParen() { return getToken(BazelBuildParser.CloseParen, 0); }
		public Target_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_target_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterTarget_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitTarget_exp(this);
		}
	}

	public final Target_expContext target_exp() throws RecognitionException {
		Target_expContext _localctx = new Target_expContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_target_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(Symbol);
			setState(34);
			match(OpenParen);
			setState(35);
			assign_items();
			setState(36);
			match(CloseParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_itemsContext extends ParserRuleContext {
		public Assign_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_items; }
	 
		public Assign_itemsContext() { }
		public void copyFrom(Assign_itemsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultiAttrContext extends Assign_itemsContext {
		public Assign_expContext assign_exp() {
			return getRuleContext(Assign_expContext.class,0);
		}
		public Assign_itemsContext assign_items() {
			return getRuleContext(Assign_itemsContext.class,0);
		}
		public MultiAttrContext(Assign_itemsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterMultiAttr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitMultiAttr(this);
		}
	}
	public static class SingleAttrContext extends Assign_itemsContext {
		public Assign_expContext assign_exp() {
			return getRuleContext(Assign_expContext.class,0);
		}
		public SingleAttrContext(Assign_itemsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterSingleAttr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitSingleAttr(this);
		}
	}

	public final Assign_itemsContext assign_items() throws RecognitionException {
		Assign_itemsContext _localctx = new Assign_itemsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assign_items);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new SingleAttrContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				assign_exp();
				}
				break;
			case 2:
				_localctx = new MultiAttrContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				assign_exp();
				setState(40);
				match(T__0);
				setState(41);
				assign_items();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_expContext extends ParserRuleContext {
		public Token left;
		public Value_expContext right;
		public TerminalNode Symbol() { return getToken(BazelBuildParser.Symbol, 0); }
		public Value_expContext value_exp() {
			return getRuleContext(Value_expContext.class,0);
		}
		public Assign_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterAssign_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitAssign_exp(this);
		}
	}

	public final Assign_expContext assign_exp() throws RecognitionException {
		Assign_expContext _localctx = new Assign_expContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assign_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			((Assign_expContext)_localctx).left = match(Symbol);
			setState(46);
			match(T__1);
			setState(47);
			((Assign_expContext)_localctx).right = value_exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Value_expContext extends ParserRuleContext {
		public Value_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value_exp; }
	 
		public Value_expContext() { }
		public void copyFrom(Value_expContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SingleValueContext extends Value_expContext {
		public TerminalNode ShortString() { return getToken(BazelBuildParser.ShortString, 0); }
		public SingleValueContext(Value_expContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterSingleValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitSingleValue(this);
		}
	}
	public static class ListValueContext extends Value_expContext {
		public List_expContext list_exp() {
			return getRuleContext(List_expContext.class,0);
		}
		public ListValueContext(Value_expContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterListValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitListValue(this);
		}
	}

	public final Value_expContext value_exp() throws RecognitionException {
		Value_expContext _localctx = new Value_expContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_value_exp);
		try {
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ShortString:
				_localctx = new SingleValueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				match(ShortString);
				}
				break;
			case OpenBracket:
				_localctx = new ListValueContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				list_exp();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class List_expContext extends ParserRuleContext {
		public List_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_exp; }
	 
		public List_expContext() { }
		public void copyFrom(List_expContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class EmptyListValueContext extends List_expContext {
		public TerminalNode OpenBracket() { return getToken(BazelBuildParser.OpenBracket, 0); }
		public TerminalNode CloseBracket() { return getToken(BazelBuildParser.CloseBracket, 0); }
		public EmptyListValueContext(List_expContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterEmptyListValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitEmptyListValue(this);
		}
	}
	public static class NoEmptyListValueContext extends List_expContext {
		public TerminalNode OpenBracket() { return getToken(BazelBuildParser.OpenBracket, 0); }
		public Str_itemsContext str_items() {
			return getRuleContext(Str_itemsContext.class,0);
		}
		public TerminalNode CloseBracket() { return getToken(BazelBuildParser.CloseBracket, 0); }
		public NoEmptyListValueContext(List_expContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterNoEmptyListValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitNoEmptyListValue(this);
		}
	}

	public final List_expContext list_exp() throws RecognitionException {
		List_expContext _localctx = new List_expContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_list_exp);
		try {
			setState(59);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new EmptyListValueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				match(OpenBracket);
				setState(54);
				match(CloseBracket);
				}
				break;
			case 2:
				_localctx = new NoEmptyListValueContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				match(OpenBracket);
				setState(56);
				str_items();
				setState(57);
				match(CloseBracket);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Str_itemsContext extends ParserRuleContext {
		public Str_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_items; }
	 
		public Str_itemsContext() { }
		public void copyFrom(Str_itemsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SingleShortStringContext extends Str_itemsContext {
		public TerminalNode ShortString() { return getToken(BazelBuildParser.ShortString, 0); }
		public SingleShortStringContext(Str_itemsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterSingleShortString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitSingleShortString(this);
		}
	}
	public static class MultiShortStringContext extends Str_itemsContext {
		public TerminalNode ShortString() { return getToken(BazelBuildParser.ShortString, 0); }
		public Str_itemsContext str_items() {
			return getRuleContext(Str_itemsContext.class,0);
		}
		public MultiShortStringContext(Str_itemsContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterMultiShortString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitMultiShortString(this);
		}
	}

	public final Str_itemsContext str_items() throws RecognitionException {
		Str_itemsContext _localctx = new Str_itemsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_str_items);
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new SingleShortStringContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				match(ShortString);
				}
				break;
			case 2:
				_localctx = new MultiShortStringContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(62);
				match(ShortString);
				setState(63);
				match(T__0);
				setState(64);
				str_items();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20F\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26"+
		"\n\2\r\2\16\2\27\3\3\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6.\n\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\66"+
		"\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t>\n\t\3\n\3\n\3\n\3\n\5\nD\n\n\3\n\2\2"+
		"\13\2\4\6\b\n\f\16\20\22\2\2\2C\2\25\3\2\2\2\4\34\3\2\2\2\6\36\3\2\2\2"+
		"\b#\3\2\2\2\n-\3\2\2\2\f/\3\2\2\2\16\65\3\2\2\2\20=\3\2\2\2\22C\3\2\2"+
		"\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2"+
		"\2\30\3\3\2\2\2\31\35\5\6\4\2\32\35\5\b\5\2\33\35\7\t\2\2\34\31\3\2\2"+
		"\2\34\32\3\2\2\2\34\33\3\2\2\2\35\5\3\2\2\2\36\37\7\20\2\2\37 \7\f\2\2"+
		" !\5\22\n\2!\"\7\r\2\2\"\7\3\2\2\2#$\7\5\2\2$%\7\f\2\2%&\5\n\6\2&\'\7"+
		"\r\2\2\'\t\3\2\2\2(.\5\f\7\2)*\5\f\7\2*+\7\3\2\2+,\5\n\6\2,.\3\2\2\2-"+
		"(\3\2\2\2-)\3\2\2\2.\13\3\2\2\2/\60\7\5\2\2\60\61\7\4\2\2\61\62\5\16\b"+
		"\2\62\r\3\2\2\2\63\66\7\b\2\2\64\66\5\20\t\2\65\63\3\2\2\2\65\64\3\2\2"+
		"\2\66\17\3\2\2\2\678\7\16\2\28>\7\17\2\29:\7\16\2\2:;\5\22\n\2;<\7\17"+
		"\2\2<>\3\2\2\2=\67\3\2\2\2=9\3\2\2\2>\21\3\2\2\2?D\7\b\2\2@A\7\b\2\2A"+
		"B\7\3\2\2BD\5\22\n\2C?\3\2\2\2C@\3\2\2\2D\23\3\2\2\2\b\27\34-\65=C";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}