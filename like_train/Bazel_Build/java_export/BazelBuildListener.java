// Generated from BazelBuild.y by ANTLR 4.7.1
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
	 * Enter a parse tree produced by the {@code LoadStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterLoadStat(BazelBuildParser.LoadStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LoadStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitLoadStat(BazelBuildParser.LoadStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TargetStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterTargetStat(BazelBuildParser.TargetStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TargetStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitTargetStat(BazelBuildParser.TargetStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LongStrStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterLongStrStat(BazelBuildParser.LongStrStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LongStrStat}
	 * labeled alternative in {@link BazelBuildParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitLongStrStat(BazelBuildParser.LongStrStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#load_exp}.
	 * @param ctx the parse tree
	 */
	void enterLoad_exp(BazelBuildParser.Load_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#load_exp}.
	 * @param ctx the parse tree
	 */
	void exitLoad_exp(BazelBuildParser.Load_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#target_exp}.
	 * @param ctx the parse tree
	 */
	void enterTarget_exp(BazelBuildParser.Target_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#target_exp}.
	 * @param ctx the parse tree
	 */
	void exitTarget_exp(BazelBuildParser.Target_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SingleAttr}
	 * labeled alternative in {@link BazelBuildParser#assign_items}.
	 * @param ctx the parse tree
	 */
	void enterSingleAttr(BazelBuildParser.SingleAttrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SingleAttr}
	 * labeled alternative in {@link BazelBuildParser#assign_items}.
	 * @param ctx the parse tree
	 */
	void exitSingleAttr(BazelBuildParser.SingleAttrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiAttr}
	 * labeled alternative in {@link BazelBuildParser#assign_items}.
	 * @param ctx the parse tree
	 */
	void enterMultiAttr(BazelBuildParser.MultiAttrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiAttr}
	 * labeled alternative in {@link BazelBuildParser#assign_items}.
	 * @param ctx the parse tree
	 */
	void exitMultiAttr(BazelBuildParser.MultiAttrContext ctx);
	/**
	 * Enter a parse tree produced by {@link BazelBuildParser#assign_exp}.
	 * @param ctx the parse tree
	 */
	void enterAssign_exp(BazelBuildParser.Assign_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link BazelBuildParser#assign_exp}.
	 * @param ctx the parse tree
	 */
	void exitAssign_exp(BazelBuildParser.Assign_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SingleValue}
	 * labeled alternative in {@link BazelBuildParser#value_exp}.
	 * @param ctx the parse tree
	 */
	void enterSingleValue(BazelBuildParser.SingleValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SingleValue}
	 * labeled alternative in {@link BazelBuildParser#value_exp}.
	 * @param ctx the parse tree
	 */
	void exitSingleValue(BazelBuildParser.SingleValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ListValue}
	 * labeled alternative in {@link BazelBuildParser#value_exp}.
	 * @param ctx the parse tree
	 */
	void enterListValue(BazelBuildParser.ListValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ListValue}
	 * labeled alternative in {@link BazelBuildParser#value_exp}.
	 * @param ctx the parse tree
	 */
	void exitListValue(BazelBuildParser.ListValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EmptyListValue}
	 * labeled alternative in {@link BazelBuildParser#list_exp}.
	 * @param ctx the parse tree
	 */
	void enterEmptyListValue(BazelBuildParser.EmptyListValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EmptyListValue}
	 * labeled alternative in {@link BazelBuildParser#list_exp}.
	 * @param ctx the parse tree
	 */
	void exitEmptyListValue(BazelBuildParser.EmptyListValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NoEmptyListValue}
	 * labeled alternative in {@link BazelBuildParser#list_exp}.
	 * @param ctx the parse tree
	 */
	void enterNoEmptyListValue(BazelBuildParser.NoEmptyListValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NoEmptyListValue}
	 * labeled alternative in {@link BazelBuildParser#list_exp}.
	 * @param ctx the parse tree
	 */
	void exitNoEmptyListValue(BazelBuildParser.NoEmptyListValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SingleShortString}
	 * labeled alternative in {@link BazelBuildParser#str_items}.
	 * @param ctx the parse tree
	 */
	void enterSingleShortString(BazelBuildParser.SingleShortStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SingleShortString}
	 * labeled alternative in {@link BazelBuildParser#str_items}.
	 * @param ctx the parse tree
	 */
	void exitSingleShortString(BazelBuildParser.SingleShortStringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiShortString}
	 * labeled alternative in {@link BazelBuildParser#str_items}.
	 * @param ctx the parse tree
	 */
	void enterMultiShortString(BazelBuildParser.MultiShortStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiShortString}
	 * labeled alternative in {@link BazelBuildParser#str_items}.
	 * @param ctx the parse tree
	 */
	void exitMultiShortString(BazelBuildParser.MultiShortStringContext ctx);
}