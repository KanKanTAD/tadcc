// Generated from .\Calculantlr.y by ANTLR 4.9
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CalculantlrParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CalculantlrVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by the {@code AtomExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtomExpr(CalculantlrParser.AtomExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenExpr(CalculantlrParser.ParenExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code OpExpr}
	 * labeled alternative in {@link CalculantlrParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOpExpr(CalculantlrParser.OpExprContext ctx);
}