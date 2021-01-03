// Generated from BazelBuild.g4 by ANTLR 4.9
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
	static { RuntimeMetaData.checkVersion("4.9", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, ID=7, StringValue=8, Whitespace=9, 
		Newline=10, BlockComment=11, LineComment=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ID", "StringValue", 
			"Whitespace", "Newline", "BlockComment", "LineComment"
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


	public BazelBuildLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BazelBuild.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16{\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3"+
		"\b\3\b\7\b*\n\b\f\b\16\b-\13\b\3\t\3\t\3\t\3\t\7\t\63\n\t\f\t\16\t\66"+
		"\13\t\3\t\3\t\3\t\3\t\3\t\7\t=\n\t\f\t\16\t@\13\t\3\t\5\tC\n\t\3\n\6\n"+
		"F\n\n\r\n\16\nG\3\n\3\n\3\13\3\13\5\13N\n\13\3\13\5\13Q\n\13\3\13\3\13"+
		"\3\f\3\f\3\f\3\f\3\f\7\fZ\n\f\f\f\16\f]\13\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\7\fg\n\f\f\f\16\fj\13\f\3\f\3\f\3\f\5\fo\n\f\3\f\3\f\3\r\3\r\7"+
		"\ru\n\r\f\r\16\rx\13\r\3\r\3\r\6\64>[h\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\3\2\t\5\2C\\aac|\6\2\62;C\\aac|\5\2\f\f"+
		"\16\17$$\5\2\f\f\16\17))\4\2\13\13\"\"\4\2\f\f\16\16\4\2\f\f\16\17\2\u0087"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3"+
		"\2\2\2\r%\3\2\2\2\17\'\3\2\2\2\21B\3\2\2\2\23E\3\2\2\2\25P\3\2\2\2\27"+
		"n\3\2\2\2\31r\3\2\2\2\33\34\7*\2\2\34\4\3\2\2\2\35\36\7+\2\2\36\6\3\2"+
		"\2\2\37 \7.\2\2 \b\3\2\2\2!\"\7?\2\2\"\n\3\2\2\2#$\7]\2\2$\f\3\2\2\2%"+
		"&\7_\2\2&\16\3\2\2\2\'+\t\2\2\2(*\t\3\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2"+
		"\2+,\3\2\2\2,\20\3\2\2\2-+\3\2\2\2.\64\7$\2\2/\60\7^\2\2\60\63\7$\2\2"+
		"\61\63\n\4\2\2\62/\3\2\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\65\3\2\2\2\64"+
		"\62\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\67C\7$\2\28>\7)\2\29:\7^\2\2:"+
		"=\7)\2\2;=\n\5\2\2<9\3\2\2\2<;\3\2\2\2=@\3\2\2\2>?\3\2\2\2><\3\2\2\2?"+
		"A\3\2\2\2@>\3\2\2\2AC\7)\2\2B.\3\2\2\2B8\3\2\2\2C\22\3\2\2\2DF\t\6\2\2"+
		"ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\b\n\2\2J\24\3\2\2"+
		"\2KM\7\17\2\2LN\7\f\2\2ML\3\2\2\2MN\3\2\2\2NQ\3\2\2\2OQ\t\7\2\2PK\3\2"+
		"\2\2PO\3\2\2\2QR\3\2\2\2RS\b\13\2\2S\26\3\2\2\2TU\7$\2\2UV\7$\2\2VW\7"+
		"$\2\2W[\3\2\2\2XZ\13\2\2\2YX\3\2\2\2Z]\3\2\2\2[\\\3\2\2\2[Y\3\2\2\2\\"+
		"^\3\2\2\2][\3\2\2\2^_\7$\2\2_`\7$\2\2`o\7$\2\2ab\7)\2\2bc\7)\2\2cd\7)"+
		"\2\2dh\3\2\2\2eg\13\2\2\2fe\3\2\2\2gj\3\2\2\2hi\3\2\2\2hf\3\2\2\2ik\3"+
		"\2\2\2jh\3\2\2\2kl\7)\2\2lm\7)\2\2mo\7)\2\2nT\3\2\2\2na\3\2\2\2op\3\2"+
		"\2\2pq\b\f\2\2q\30\3\2\2\2rv\7%\2\2su\n\b\2\2ts\3\2\2\2ux\3\2\2\2vt\3"+
		"\2\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\b\r\2\2z\32\3\2\2\2\20\2+\62\64"+
		"<>BGMP[hnv\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}