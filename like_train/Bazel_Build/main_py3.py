import antlr4 as antlr
import sys
from dist_py3.BazelBuildLexer import BazelBuildLexer
from dist_py3.BazelBuildParser import BazelBuildParser
from dist_py3.BazelBuildVisitor import BazelBuildVisitor


class MyVisitor(BazelBuildVisitor):
    pass


def main(f: str = None):
    if f is None:
        stream = antlr.StdinStream()
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
