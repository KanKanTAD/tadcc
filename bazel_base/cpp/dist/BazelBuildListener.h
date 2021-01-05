
// Generated from ./BazelBuild.g4 by ANTLR 4.9

#pragma once


#include "antlr4-runtime.h"
#include "BazelBuildParser.h"


/**
 * This interface defines an abstract listener for a parse tree produced by BazelBuildParser.
 */
class  BazelBuildListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterProg(BazelBuildParser::ProgContext *ctx) = 0;
  virtual void exitProg(BazelBuildParser::ProgContext *ctx) = 0;

  virtual void enterStat(BazelBuildParser::StatContext *ctx) = 0;
  virtual void exitStat(BazelBuildParser::StatContext *ctx) = 0;

  virtual void enterArglist(BazelBuildParser::ArglistContext *ctx) = 0;
  virtual void exitArglist(BazelBuildParser::ArglistContext *ctx) = 0;

  virtual void enterArgument(BazelBuildParser::ArgumentContext *ctx) = 0;
  virtual void exitArgument(BazelBuildParser::ArgumentContext *ctx) = 0;

  virtual void enterValue(BazelBuildParser::ValueContext *ctx) = 0;
  virtual void exitValue(BazelBuildParser::ValueContext *ctx) = 0;

  virtual void enterMulti_value(BazelBuildParser::Multi_valueContext *ctx) = 0;
  virtual void exitMulti_value(BazelBuildParser::Multi_valueContext *ctx) = 0;

  virtual void enterVal_list(BazelBuildParser::Val_listContext *ctx) = 0;
  virtual void exitVal_list(BazelBuildParser::Val_listContext *ctx) = 0;

  virtual void enterSingle_value(BazelBuildParser::Single_valueContext *ctx) = 0;
  virtual void exitSingle_value(BazelBuildParser::Single_valueContext *ctx) = 0;


};

