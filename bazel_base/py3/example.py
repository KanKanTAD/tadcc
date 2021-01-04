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
    def visitProg(self, ctx: BazelBuildParser.ProgContext) -> BazelBuild:
        b = BazelBuild()
        ms = ctx.stat()
        ms = [] if ms is None else [self.visit(m) for m in ms]
        b.set_call_metis(ms)
        return b

    # Visit a parse tree produced by BazelBuildParser#stat.
    def visitStat(self, ctx: BazelBuildParser.StatContext):
        name = ctx.ID()
        name = "" if name is None else name.getText()
        a_list = ctx.arglist()
        a_list = [] if a_list is None else self.visit(a_list)
        c = CallMeta()
        c.set_funcname(name)
        c.set_arglist(a_list)
        return c

    # Visit a parse tree produced by BazelBuildParser#arglist.
    def visitArglist(self, ctx: BazelBuildParser.ArglistContext):
        return [self.visit(a) for a in ctx.argument()]

    # Visit a parse tree produced by BazelBuildParser#argument.
    def visitArgument(self, ctx: BazelBuildParser.ArgumentContext):
        name = ctx.ID()
        name = "" if name is None else name.getText()
        value = self.visit(ctx.value())
        a = Argument()
        a.set_name(name)
        a.set_value(value)
        return a

    # Visit a parse tree produced by BazelBuildParser#singleV.
    def visitSingleV(self, ctx: BazelBuildParser.SingleVContext):
        v = self.visit(ctx.single_value())
        return SingleValue(v)

    # Visit a parse tree produced by BazelBuildParser#multiV.
    def visitMultiV(self, ctx: BazelBuildParser.MultiVContext):
        return self.visit(ctx.multi_value())

    # Visit a parse tree produced by BazelBuildParser#multi_value.
    def visitMulti_value(self, ctx: BazelBuildParser.Multi_valueContext):
        v_list = ctx.val_list()
        return [] if v_list is None else self.visit(v_list)

    # Visit a parse tree produced by BazelBuildParser#val_list.
    def visitVal_list(self, ctx: BazelBuildParser.Val_listContext):
        single_values = ctx.single_value()
        return [self.visit(v) for v in single_values]

    # Visit a parse tree produced by BazelBuildParser#single_value.
    def visitSingle_value(self, ctx: BazelBuildParser.Single_valueContext):
        value = ctx.StringValue()
        return "" if value is None else value.getText()


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
    build = visitor.visit(tree)
    print(build.stringify())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read() + '\n')
    else:
        main()
