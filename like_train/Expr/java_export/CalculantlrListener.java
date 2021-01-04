// Generated from .\Calculantlr.y by ANTLR 4.9
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalculantlrParser}.
 */
public interface CalculantlrListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code AtomExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAtomExpr(CalculantlrParser.AtomExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AtomExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAtomExpr(CalculantlrParser.AtomExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(CalculantlrParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(CalculantlrParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OpExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOpExpr(CalculantlrParser.OpExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OpExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOpExpr(CalculantlrParser.OpExprContext ctx);
}