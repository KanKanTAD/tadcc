#!/usr/bin/env python2
# -*- encoding:utf8 -*-

import antlr4 as antlr
import sys
from dist.BazelBuildLexer import BazelBuildLexer
from dist.BazelBuildParser import BazelBuildParser
from dist.BazelBuildVisitor import BazelBuildVisitor
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s::%(funcName)s [line:%(lineno)d] - %(levelname)s: %(message)s')


sys.path.append('./bazel_base/bazel_base/')

from bazel_base.BazelBuild import BazelBuild
from bazel_base.SingleValue import SingleValue
from bazel_base.Argument import Argument
from bazel_base.MultiValue import MultiValue
from bazel_base.CallMeta import CallMeta

class MyVisitor(BazelBuildVisitor):
    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        res = BazelBuild()
        stats = ctx.stat()
        if stats is None:
            return res
        for s in stats:
            res.children.append(self.visit(s))
        return res

    # Visit a parse tree produced by BazelBuildParser#stat.

    def visitStat(self, ctx):
        res = CallMeta()
        res.name = ctx.ID().getText()
        arglist = ctx.arglist()
        if arglist is None:
            return res
        res.children = self.visit(arglist)
        return res

    # Visit a parse tree produced by BazelBuildParser#arglist.

    def visitArglist(self, ctx):
        res = list()
        arguments = ctx.argument()
        if arguments is None:
            return res
        for a in arguments:
            res.append(self.visit(a))
        return res

    # Visit a parse tree produced by BazelBuildParser#argument.

    def visitArgument(self, ctx):
        res = Argument()
        res.name = ctx.ID().getText()
        res.children.append(self.visit(ctx.value()))
        return res

    # Visit a parse tree produced by BazelBuildParser#value.

    def visitValue(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#multi_value.

    def visitMulti_value(self, ctx):
        res = MultiValue()
        val_list = ctx.val_list()
        if val_list is None:
            return res
        res.children = self.visit(val_list)
        return res

    # Visit a parse tree produced by BazelBuildParser#val_list.

    def visitVal_list(self, ctx):
        res = list()
        for val in ctx.single_value():
            res.append(self.visit(val))
        return res

    # Visit a parse tree produced by BazelBuildParser#single_value.

    def visitSingle_value(self, ctx):
        res = SingleValue()
        res.value = ctx.StringValue().getText()
        return res


def main(f=None):
    if f is None:
        stream = antlr.StdinStream(encoding='utf8')
    else:
        stream = antlr.InputStream(f)
    lexer = BazelBuildLexer(stream)
    token_stream = antlr.CommonTokenStream(lexer)
    parser = BazelBuildParser(token_stream)
    tree = parser.prog()
    visitor = MyVisitor()
    bb = visitor.visit(tree)
    print(bb.stringify())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read()+'\n')
    else:
        main()
