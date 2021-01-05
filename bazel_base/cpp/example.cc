#include "BazelBuildBaseVisitor.h"
#include "BazelBuildLexer.h"
#include "BazelBuildParser.h"
#include "BazelBuildVisitor.h"
#include "CharStream.h"
#include "CommonTokenStream.h"
#include <antlr4-runtime/antlr4-runtime.h>
#include <iostream>

class MyVisitor : public BazelBuildBaseVisitor {
public:
  antlrcpp::Any visitProg(BazelBuildParser::ProgContext *ctx) override {
    std::cout << "hello world" << std::endl;
    return BazelBuildBaseVisitor::visitProg(ctx);
  }
};

int main(int argc, char *argv[]) {

  antlr4::CharStream *_stream = nullptr;
  if (argc > 1) {
    _stream = new antlr4::ANTLRFileStream(argv[1]);
  } else {
    _stream = new antlr4::ANTLRInputStream(std::cin);
  }
  BazelBuildLexer lexer(_stream);
  antlr4::CommonTokenStream token_stream(&lexer);
  BazelBuildParser parser(&token_stream);
  auto tree = parser.prog();
  MyVisitor visitor;
  auto x = visitor.visit(tree);

  delete _stream;
}
