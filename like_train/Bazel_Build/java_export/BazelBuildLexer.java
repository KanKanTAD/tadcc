// Generated from BazelBuild.y by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BazelBuildLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Symbol=3, Comment=4, WS=5, ShortString=6, LongString=7, 
		LongStringItem=8, RN=9, OpenParen=10, CloseParen=11, OpenBracket=12, CloseBracket=13, 
		Load=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "Symbol", "Comment", "WS", "ShortString", "LongString", 
		"LongStringItem", "RN", "OpenParen", "CloseParen", "OpenBracket", "CloseBracket", 
		"Load"
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


	public BazelBuildLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BazelBuild.y"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20\u0090\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\6\4%"+
		"\n\4\r\4\16\4&\3\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\7\5\61\n\5\f\5\16\5"+
		"\64\13\5\3\5\3\5\3\6\6\69\n\6\r\6\16\6:\3\6\3\6\3\7\3\7\3\7\3\7\5\7C\n"+
		"\7\3\7\7\7F\n\7\f\7\16\7I\13\7\3\7\3\7\3\7\3\7\3\7\5\7P\n\7\3\7\7\7S\n"+
		"\7\f\7\16\7V\13\7\3\7\5\7Y\n\7\3\b\3\b\3\b\3\b\3\b\7\b`\n\b\f\b\16\bc"+
		"\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bm\n\b\f\b\16\bp\13\b\3\b\3\b"+
		"\3\b\5\bu\n\b\3\t\3\t\3\t\3\t\5\t{\n\t\5\t}\n\t\3\n\5\n\u0080\n\n\3\n"+
		"\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\4an"+
		"\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\3\2\t\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\16\17\5\2\13\f\17\17\"\"\6"+
		"\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\3\2^^\2\u00a0\2\3\3\2\2\2\2\5\3\2\2"+
		"\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7$\3\2\2\2\t.\3\2\2\2\138\3"+
		"\2\2\2\rX\3\2\2\2\17t\3\2\2\2\21|\3\2\2\2\23\177\3\2\2\2\25\u0083\3\2"+
		"\2\2\27\u0085\3\2\2\2\31\u0087\3\2\2\2\33\u0089\3\2\2\2\35\u008b\3\2\2"+
		"\2\37 \7.\2\2 \4\3\2\2\2!\"\7?\2\2\"\6\3\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3"+
		"\2\2\2&$\3\2\2\2&\'\3\2\2\2\'+\3\2\2\2(*\t\3\2\2)(\3\2\2\2*-\3\2\2\2+"+
		")\3\2\2\2+,\3\2\2\2,\b\3\2\2\2-+\3\2\2\2.\62\7%\2\2/\61\n\4\2\2\60/\3"+
		"\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3"+
		"\2\2\2\65\66\b\5\2\2\66\n\3\2\2\2\679\t\5\2\28\67\3\2\2\29:\3\2\2\2:8"+
		"\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\6\2\2=\f\3\2\2\2>G\7)\2\2?B\7^\2\2@C"+
		"\5\23\n\2AC\13\2\2\2B@\3\2\2\2BA\3\2\2\2CF\3\2\2\2DF\n\6\2\2E?\3\2\2\2"+
		"ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JY\7)\2\2"+
		"KT\7$\2\2LO\7^\2\2MP\5\23\n\2NP\13\2\2\2OM\3\2\2\2ON\3\2\2\2PS\3\2\2\2"+
		"QS\n\7\2\2RL\3\2\2\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2"+
		"VT\3\2\2\2WY\7$\2\2X>\3\2\2\2XK\3\2\2\2Y\16\3\2\2\2Z[\7)\2\2[\\\7)\2\2"+
		"\\]\7)\2\2]a\3\2\2\2^`\5\21\t\2_^\3\2\2\2`c\3\2\2\2ab\3\2\2\2a_\3\2\2"+
		"\2bd\3\2\2\2ca\3\2\2\2de\7)\2\2ef\7)\2\2fu\7)\2\2gh\7$\2\2hi\7$\2\2ij"+
		"\7$\2\2jn\3\2\2\2km\5\21\t\2lk\3\2\2\2mp\3\2\2\2no\3\2\2\2nl\3\2\2\2o"+
		"q\3\2\2\2pn\3\2\2\2qr\7$\2\2rs\7$\2\2su\7$\2\2tZ\3\2\2\2tg\3\2\2\2u\20"+
		"\3\2\2\2v}\n\b\2\2wz\7^\2\2x{\5\23\n\2y{\13\2\2\2zx\3\2\2\2zy\3\2\2\2"+
		"{}\3\2\2\2|v\3\2\2\2|w\3\2\2\2}\22\3\2\2\2~\u0080\7\17\2\2\177~\3\2\2"+
		"\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7\f\2\2\u0082\24"+
		"\3\2\2\2\u0083\u0084\7*\2\2\u0084\26\3\2\2\2\u0085\u0086\7+\2\2\u0086"+
		"\30\3\2\2\2\u0087\u0088\7]\2\2\u0088\32\3\2\2\2\u0089\u008a\7_\2\2\u008a"+
		"\34\3\2\2\2\u008b\u008c\7n\2\2\u008c\u008d\7q\2\2\u008d\u008e\7c\2\2\u008e"+
		"\u008f\7f\2\2\u008f\36\3\2\2\2\24\2&+\62:BEGORTXantz|\177\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}