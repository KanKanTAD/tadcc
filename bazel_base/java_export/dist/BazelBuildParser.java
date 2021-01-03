// Generated from BazelBuild.g4 by ANTLR 4.9
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
	static { RuntimeMetaData.checkVersion("4.9", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, ID=7, StringValue=8, Whitespace=9, 
		Newline=10, BlockComment=11, LineComment=12;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_arglist = 2, RULE_argument = 3, RULE_value = 4, 
		RULE_multi_value = 5, RULE_val_list = 6, RULE_single_value = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "arglist", "argument", "value", "multi_value", "val_list", 
			"single_value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "','", "'='", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "ID", "StringValue", "Whitespace", 
			"Newline", "BlockComment", "LineComment"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "BazelBuild.g4"; }

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
			while (_la==ID) {
				{
				{
				setState(16);
				stat();
				}
				}
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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
		public TerminalNode ID() { return getToken(BazelBuildParser.ID, 0); }
		public TerminalNode Newline() { return getToken(BazelBuildParser.Newline, 0); }
		public ArglistContext arglist() {
			return getRuleContext(ArglistContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(ID);
			setState(23);
			match(T__0);
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(24);
				arglist();
				}
			}

			setState(27);
			match(T__1);
			setState(28);
			match(Newline);
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

	public static class ArglistContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public ArglistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arglist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterArglist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitArglist(this);
		}
	}

	public final ArglistContext arglist() throws RecognitionException {
		ArglistContext _localctx = new ArglistContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_arglist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			argument();
			setState(35);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(31);
					match(T__2);
					setState(32);
					argument();
					}
					} 
				}
				setState(37);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(38);
				match(T__2);
				}
			}

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

	public static class ArgumentContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode ID() { return getToken(BazelBuildParser.ID, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitArgument(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_argument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(41);
			match(ID);
			setState(42);
			match(T__3);
			}
			setState(44);
			value();
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

	public static class ValueContext extends ParserRuleContext {
		public Single_valueContext single_value() {
			return getRuleContext(Single_valueContext.class,0);
		}
		public Multi_valueContext multi_value() {
			return getRuleContext(Multi_valueContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_value);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case StringValue:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				single_value();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				multi_value();
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

	public static class Multi_valueContext extends ParserRuleContext {
		public Val_listContext val_list() {
			return getRuleContext(Val_listContext.class,0);
		}
		public Multi_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multi_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterMulti_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitMulti_value(this);
		}
	}

	public final Multi_valueContext multi_value() throws RecognitionException {
		Multi_valueContext _localctx = new Multi_valueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_multi_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(T__4);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==StringValue) {
				{
				setState(51);
				val_list();
				}
			}

			setState(54);
			match(T__5);
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

	public static class Val_listContext extends ParserRuleContext {
		public List<Single_valueContext> single_value() {
			return getRuleContexts(Single_valueContext.class);
		}
		public Single_valueContext single_value(int i) {
			return getRuleContext(Single_valueContext.class,i);
		}
		public Val_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_val_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterVal_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitVal_list(this);
		}
	}

	public final Val_listContext val_list() throws RecognitionException {
		Val_listContext _localctx = new Val_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_val_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			single_value();
			setState(61);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(57);
					match(T__2);
					setState(58);
					single_value();
					}
					} 
				}
				setState(63);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(64);
				match(T__2);
				}
			}

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

	public static class Single_valueContext extends ParserRuleContext {
		public TerminalNode StringValue() { return getToken(BazelBuildParser.StringValue, 0); }
		public Single_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).enterSingle_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BazelBuildListener ) ((BazelBuildListener)listener).exitSingle_value(this);
		}
	}

	public final Single_valueContext single_value() throws RecognitionException {
		Single_valueContext _localctx = new Single_valueContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_single_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(StringValue);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16H\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2"+
		"\16\2\27\13\2\3\3\3\3\3\3\5\3\34\n\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4$\n\4"+
		"\f\4\16\4\'\13\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6\63\n\6\3"+
		"\7\3\7\5\7\67\n\7\3\7\3\7\3\b\3\b\3\b\7\b>\n\b\f\b\16\bA\13\b\3\b\5\b"+
		"D\n\b\3\t\3\t\3\t\4%?\2\n\2\4\6\b\n\f\16\20\2\2\2G\2\25\3\2\2\2\4\30\3"+
		"\2\2\2\6 \3\2\2\2\b+\3\2\2\2\n\62\3\2\2\2\f\64\3\2\2\2\16:\3\2\2\2\20"+
		"E\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26"+
		"\3\2\2\2\26\3\3\2\2\2\27\25\3\2\2\2\30\31\7\t\2\2\31\33\7\3\2\2\32\34"+
		"\5\6\4\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\7\4\2\2\36\37"+
		"\7\f\2\2\37\5\3\2\2\2 %\5\b\5\2!\"\7\5\2\2\"$\5\b\5\2#!\3\2\2\2$\'\3\2"+
		"\2\2%&\3\2\2\2%#\3\2\2\2&)\3\2\2\2\'%\3\2\2\2(*\7\5\2\2)(\3\2\2\2)*\3"+
		"\2\2\2*\7\3\2\2\2+,\7\t\2\2,-\7\6\2\2-.\3\2\2\2./\5\n\6\2/\t\3\2\2\2\60"+
		"\63\5\20\t\2\61\63\5\f\7\2\62\60\3\2\2\2\62\61\3\2\2\2\63\13\3\2\2\2\64"+
		"\66\7\7\2\2\65\67\5\16\b\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7"+
		"\b\2\29\r\3\2\2\2:?\5\20\t\2;<\7\5\2\2<>\5\20\t\2=;\3\2\2\2>A\3\2\2\2"+
		"?@\3\2\2\2?=\3\2\2\2@C\3\2\2\2A?\3\2\2\2BD\7\5\2\2CB\3\2\2\2CD\3\2\2\2"+
		"D\17\3\2\2\2EF\7\n\2\2F\21\3\2\2\2\n\25\33%)\62\66?C";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}