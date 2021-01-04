#!/usr/bin/env python3

from BazelBase.base.base.BazelBuild import BazelBuild
from BazelBase.base.base.CallMeta import CallMeta
from BazelBase.base.base.Value import Value
from BazelBase.base.base.SingleValue import SingleValue
from BazelBase.base.base.MultiValue import MultiValue

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

    # Visit a parse tree produced by BazelBuildParser#singleV.
    def visitSingleV(self, ctx: BazelBuildParser.SingleVContext):
        v = self.visit(ctx.single_value())
        return SingleValue(v)

    # Visit a parse tree produced by BazelBuildParser#multiV.
    def visitMultiV(self, ctx: BazelBuildParser.MultiVContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#multi_value.
    def visitMulti_value(self, ctx: BazelBuildParser.Multi_valueContext):
        value = self.visit(ctx.val_list())
        return "" if value is None else value

    # Visit a parse tree produced by BazelBuildParser#val_list.
    def visitVal_list(self, ctx: BazelBuildParser.Val_listContext):
        single_values = ctx.single_value()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#single_value.
    def visitSingle_value(self, ctx: BazelBuildParser.Single_valueContext):
        value = ctx.StringValue()
        if value is None:
            return ""
        else:
            return value.getText()


def main(data=None):
    if data is None:
        stream = antlr.StdinStream(encoding='utf8')
    else:
        stream = antlr.InputStream(data)
    lexer = BazelBuildLexer(stream)
    token_stream = antlr.CommonTokenStream(lexer)
    parser = BazelBuildParser(token_stream)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read() + '\n')
    else:
        main()
