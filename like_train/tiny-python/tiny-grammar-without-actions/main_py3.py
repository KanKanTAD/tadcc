import antlr4 as antlr
import sys
from dist_py3.Python3Lexer import Python3Lexer
from dist_py3.Python3Parser import Python3Parser
from dist_py3.Python3Visitor import Python3Visitor


class MyVisitor(Python3Visitor):
    pass


def main(f: str = None):
    if f is None:
        stream = antlr.StdinStream()
    else:
        stream = antlr.InputStream(f)
    lexer = Python3Lexer(stream)
    token_stream = antlr.CommonTokenStream(lexer)
    parser = Python3Parser(token_stream)
    tree = parser.stmt()
    visitor = MyVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            main(f.read()+'\n')
    else:
        main()
