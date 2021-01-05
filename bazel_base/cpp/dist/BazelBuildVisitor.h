
// Generated from ./BazelBuild.g4 by ANTLR 4.9

#pragma once


#include "antlr4-runtime.h"
#include "BazelBuildParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BazelBuildParser.
 */
class  BazelBuildVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BazelBuildParser.
   */
    virtual antlrcpp::Any visitProg(BazelBuildParser::ProgContext *context) = 0;

    virtual antlrcpp::Any visitStat(BazelBuildParser::StatContext *context) = 0;

    virtual antlrcpp::Any visitArglist(BazelBuildParser::ArglistContext *context) = 0;

    virtual antlrcpp::Any visitArgument(BazelBuildParser::ArgumentContext *context) = 0;

    virtual antlrcpp::Any visitValue(BazelBuildParser::ValueContext *context) = 0;

    virtual antlrcpp::Any visitMulti_value(BazelBuildParser::Multi_valueContext *context) = 0;

    virtual antlrcpp::Any visitVal_list(BazelBuildParser::Val_listContext *context) = 0;

    virtual antlrcpp::Any visitSingle_value(BazelBuildParser::Single_valueContext *context) = 0;


};

