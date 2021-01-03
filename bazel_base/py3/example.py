#!/usr/bin/env python3

import sys
from dist.BazelBuildLexer import BazelBuildLexer
from dist.BazelBuildParser import BazelBuildParser
from dist.BazelBuildVisitor import BazelBuildVisitor
import antlr4 as antlr


class MyVisitor(BazelBuildVisitor):
    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx: BazelBuildParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#stat.
    def visitStat(self, ctx: BazelBuildParser.StatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#arglist.
    def visitArglist(self, ctx: BazelBuildParser.ArglistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx: BazelBuildParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#value.
    def visitValue(self, ctx: BazelBuildParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#multi_value.
    def visitMulti_value(self, ctx: BazelBuildParser.Multi_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#val_list.
    def visitVal_list(self, ctx: BazelBuildParser.Val_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#single_value.
    def visitSingle_value(self, ctx: BazelBuildParser.Single_valueContext):
        token = ctx.StringValue()
        if token:
            print(token.getText())
        return self.visitChildren(ctx)


def main(data=None):
    if data is None:
        stream = antlr.StdinStream(encoding='utf8')
    else:
        stream = antlr.InputStream(data)
    lexer = BazelBuildLexer(stream)
    token_stream = antlr.CommonTokenStream(lexer)
    parser = BazelBuildParser(token_stream)
    tree = parser.prog()
    visitor = BazelBuildVisitor()
    visitor.visit(tree)
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read() + '\n')
    else:
        main()
