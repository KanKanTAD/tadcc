// Generated from BazelBuild.g4 by ANTLR 4.9
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BazelBuildParser}.
 */
public interface BazelBuildListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(BazelBuildParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(BazelBuildParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(BazelBuildParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(BazelBuildParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#arglist}.
	 * @param ctx the parse tree
	 */
	void enterArglist(BazelBuildParser.ArglistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#arglist}.
	 * @param ctx the parse tree
	 */
	void exitArglist(BazelBuildParser.ArglistContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(BazelBuildParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(BazelBuildParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(BazelBuildParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(BazelBuildParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#multi_value}.
	 * @param ctx the parse tree
	 */
	void enterMulti_value(BazelBuildParser.Multi_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#multi_value}.
	 * @param ctx the parse tree
	 */
	void exitMulti_value(BazelBuildParser.Multi_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#val_list}.
	 * @param ctx the parse tree
	 */
	void enterVal_list(BazelBuildParser.Val_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#val_list}.
	 * @param ctx the parse tree
	 */
	void exitVal_list(BazelBuildParser.Val_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#single_value}.
	 * @param ctx the parse tree
	 */
	void enterSingle_value(BazelBuildParser.Single_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#single_value}.
	 * @param ctx the parse tree
	 */
	void exitSingle_value(BazelBuildParser.Single_valueContext ctx);
}