
// Generated from ./BazelBuild.g4 by ANTLR 4.9

#pragma once


#include "antlr4-runtime.h"
#include "BazelBuildVisitor.h"


/**
 * This class provides an empty implementation of BazelBuildVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BazelBuildBaseVisitor : public BazelBuildVisitor {
public:

  virtual antlrcpp::Any visitProg(BazelBuildParser::ProgContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStat(BazelBuildParser::StatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitArglist(BazelBuildParser::ArglistContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitArgument(BazelBuildParser::ArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitValue(BazelBuildParser::ValueContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitMulti_value(BazelBuildParser::Multi_valueContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitVal_list(BazelBuildParser::Val_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitSingle_value(BazelBuildParser::Single_valueContext *ctx) override {
    return visitChildren(ctx);
  }


};

