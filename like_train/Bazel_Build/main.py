#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import antlr4 as antlr
from dist.BazelBuildLexer import BazelBuildLexer
from dist.BazelBuildParser import BazelBuildParser
from dist.BazelBuildVisitor import BazelBuildVisitor


class BazelVisitor(BazelBuildVisitor):
    pass


def main(f=None):
    if f is None:
        stream = antlr.StdinStream()
    else:
        stream = antlr.InputStream(f)

    lexer = BazelBuildLexer(stream)
    token_stream = antlr.CommonTokenStream(lexer)
    parser = BazelBuildParser(token_stream)

    tree = parser.prog()
    vi = BazelBuildVisitor()
    vi.visit(tree)


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        with open(sys.argv[1]) as f:
            main(f.read())
    else:
        main()
