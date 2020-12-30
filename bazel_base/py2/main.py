#!/usr/bin/env python2
# -*- encoding:utf8 -*-

import bazel_base
import antlr4 as antlr
import sys
from dist.BazelBuildLexer import BazelBuildLexer
from dist.BazelBuildParser import BazelBuildParser
from dist.BazelBuildVisitor import BazelBuildVisitor
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s::%(funcName)s [line:%(lineno)d] - %(levelname)s: %(message)s')


class MyVisitor(BazelBuildVisitor):

    # Visit a parse tree produced by BazelBuildParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#stat.

    def visitStat(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#action_exp.

    def visitAction_exp(self, ctx):
        name = ctx.KEY_WORD().getText()
        arglist = self.visit(ctx.str_list())
        action = bazel_base.Action(name, args=arglist)
        logging.debug(action.stringify())

    # Visit a parse tree produced by BazelBuildParser#target_exp.

    def visitTarget_exp(self, ctx):
        name = ctx.NAME()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#key_word.

    def visitKey_word(self, ctx):
        pass

    # Visit a parse tree produced by BazelBuildParser#assign_list.

    def visitAssign_list(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#assign_exp.

    def visitAssign_exp(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#value_exp.

    def visitValue_exp(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#str_list.
    def visitStr_list(self, ctx):
        return [s.getText() for s in ctx.STRING()]


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
    visitor.visit(tree)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read()+'\n')
    else:
        main()
