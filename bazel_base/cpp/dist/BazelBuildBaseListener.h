
// Generated from ./BazelBuild.g4 by ANTLR 4.9

#pragma once


#include "antlr4-runtime.h"
#include "BazelBuildListener.h"


/**
 * This class provides an empty implementation of BazelBuildListener,
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
class  BazelBuildBaseListener : public BazelBuildListener {
public:

  virtual void enterProg(BazelBuildParser::ProgContext * /*ctx*/) override { }
  virtual void exitProg(BazelBuildParser::ProgContext * /*ctx*/) override { }

  virtual void enterStat(BazelBuildParser::StatContext * /*ctx*/) override { }
  virtual void exitStat(BazelBuildParser::StatContext * /*ctx*/) override { }

  virtual void enterArglist(BazelBuildParser::ArglistContext * /*ctx*/) override { }
  virtual void exitArglist(BazelBuildParser::ArglistContext * /*ctx*/) override { }

  virtual void enterArgument(BazelBuildParser::ArgumentContext * /*ctx*/) override { }
  virtual void exitArgument(BazelBuildParser::ArgumentContext * /*ctx*/) override { }

  virtual void enterValue(BazelBuildParser::ValueContext * /*ctx*/) override { }
  virtual void exitValue(BazelBuildParser::ValueContext * /*ctx*/) override { }

  virtual void enterMulti_value(BazelBuildParser::Multi_valueContext * /*ctx*/) override { }
  virtual void exitMulti_value(BazelBuildParser::Multi_valueContext * /*ctx*/) override { }

  virtual void enterVal_list(BazelBuildParser::Val_listContext * /*ctx*/) override { }
  virtual void exitVal_list(BazelBuildParser::Val_listContext * /*ctx*/) override { }

  virtual void enterSingle_value(BazelBuildParser::Single_valueContext * /*ctx*/) override { }
  virtual void exitSingle_value(BazelBuildParser::Single_valueContext * /*ctx*/) override { }


  virtual void enterEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void exitEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void visitTerminal(antlr4::tree::TerminalNode * /*node*/) override { }
  virtual void visitErrorNode(antlr4::tree::ErrorNode * /*node*/) override { }

};

