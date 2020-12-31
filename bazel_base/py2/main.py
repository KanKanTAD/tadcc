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
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#stat.

    def visitStat(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#single_exp.

    def visitSingle_exp(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#call_exp.

    def visitCall_exp(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#argument_list.

    def visitArgument_list(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#argument.

    def visitArgument(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#signle_value.

    def visitSignle_value(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#multi_value.

    def visitMulti_value(self, ctx):
        logging.debug(' ')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BazelBuildParser#str_list.

    def visitStr_list(self, ctx):
        return self.visitChildren(ctx)


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
