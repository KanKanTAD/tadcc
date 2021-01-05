
// Generated from ./BazelBuild.g4 by ANTLR 4.9


#include "BazelBuildListener.h"
#include "BazelBuildVisitor.h"

#include "BazelBuildParser.h"


using namespace antlrcpp;
using namespace antlr4;

BazelBuildParser::BazelBuildParser(TokenStream *input) : Parser(input) {
  _interpreter = new atn::ParserATNSimulator(this, _atn, _decisionToDFA, _sharedContextCache);
}

BazelBuildParser::~BazelBuildParser() {
  delete _interpreter;
}

std::string BazelBuildParser::getGrammarFileName() const {
  return "BazelBuild.g4";
}

const std::vector<std::string>& BazelBuildParser::getRuleNames() const {
  return _ruleNames;
}

dfa::Vocabulary& BazelBuildParser::getVocabulary() const {
  return _vocabulary;
}


//----------------- ProgContext ------------------------------------------------------------------

BazelBuildParser::ProgContext::ProgContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BazelBuildParser::StatContext *> BazelBuildParser::ProgContext::stat() {
  return getRuleContexts<BazelBuildParser::StatContext>();
}

BazelBuildParser::StatContext* BazelBuildParser::ProgContext::stat(size_t i) {
  return getRuleContext<BazelBuildParser::StatContext>(i);
}


size_t BazelBuildParser::ProgContext::getRuleIndex() const {
  return BazelBuildParser::RuleProg;
}

void BazelBuildParser::ProgContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterProg(this);
}

void BazelBuildParser::ProgContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitProg(this);
}


antlrcpp::Any BazelBuildParser::ProgContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitProg(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::ProgContext* BazelBuildParser::prog() {
  ProgContext *_localctx = _tracker.createInstance<ProgContext>(_ctx, getState());
  enterRule(_localctx, 0, BazelBuildParser::RuleProg);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(19);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BazelBuildParser::ID) {
      setState(16);
      stat();
      setState(21);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StatContext ------------------------------------------------------------------

BazelBuildParser::StatContext::StatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BazelBuildParser::StatContext::ID() {
  return getToken(BazelBuildParser::ID, 0);
}

BazelBuildParser::ArglistContext* BazelBuildParser::StatContext::arglist() {
  return getRuleContext<BazelBuildParser::ArglistContext>(0);
}

std::vector<tree::TerminalNode *> BazelBuildParser::StatContext::Newline() {
  return getTokens(BazelBuildParser::Newline);
}

tree::TerminalNode* BazelBuildParser::StatContext::Newline(size_t i) {
  return getToken(BazelBuildParser::Newline, i);
}


size_t BazelBuildParser::StatContext::getRuleIndex() const {
  return BazelBuildParser::RuleStat;
}

void BazelBuildParser::StatContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStat(this);
}

void BazelBuildParser::StatContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStat(this);
}


antlrcpp::Any BazelBuildParser::StatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitStat(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::StatContext* BazelBuildParser::stat() {
  StatContext *_localctx = _tracker.createInstance<StatContext>(_ctx, getState());
  enterRule(_localctx, 2, BazelBuildParser::RuleStat);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(22);
    match(BazelBuildParser::ID);
    setState(23);
    match(BazelBuildParser::T__0);
    setState(25);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BazelBuildParser::ID) {
      setState(24);
      arglist();
    }
    setState(27);
    match(BazelBuildParser::T__1);
    setState(31);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(28);
        match(BazelBuildParser::Newline); 
      }
      setState(33);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArglistContext ------------------------------------------------------------------

BazelBuildParser::ArglistContext::ArglistContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BazelBuildParser::ArgumentContext *> BazelBuildParser::ArglistContext::argument() {
  return getRuleContexts<BazelBuildParser::ArgumentContext>();
}

BazelBuildParser::ArgumentContext* BazelBuildParser::ArglistContext::argument(size_t i) {
  return getRuleContext<BazelBuildParser::ArgumentContext>(i);
}


size_t BazelBuildParser::ArglistContext::getRuleIndex() const {
  return BazelBuildParser::RuleArglist;
}

void BazelBuildParser::ArglistContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterArglist(this);
}

void BazelBuildParser::ArglistContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitArglist(this);
}


antlrcpp::Any BazelBuildParser::ArglistContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitArglist(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::ArglistContext* BazelBuildParser::arglist() {
  ArglistContext *_localctx = _tracker.createInstance<ArglistContext>(_ctx, getState());
  enterRule(_localctx, 4, BazelBuildParser::RuleArglist);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(34);
    argument();
    setState(39);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(35);
        match(BazelBuildParser::T__2);
        setState(36);
        argument(); 
      }
      setState(41);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    }
    setState(43);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BazelBuildParser::T__2) {
      setState(42);
      match(BazelBuildParser::T__2);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgumentContext ------------------------------------------------------------------

BazelBuildParser::ArgumentContext::ArgumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BazelBuildParser::ValueContext* BazelBuildParser::ArgumentContext::value() {
  return getRuleContext<BazelBuildParser::ValueContext>(0);
}

tree::TerminalNode* BazelBuildParser::ArgumentContext::ID() {
  return getToken(BazelBuildParser::ID, 0);
}


size_t BazelBuildParser::ArgumentContext::getRuleIndex() const {
  return BazelBuildParser::RuleArgument;
}

void BazelBuildParser::ArgumentContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterArgument(this);
}

void BazelBuildParser::ArgumentContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitArgument(this);
}


antlrcpp::Any BazelBuildParser::ArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitArgument(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::ArgumentContext* BazelBuildParser::argument() {
  ArgumentContext *_localctx = _tracker.createInstance<ArgumentContext>(_ctx, getState());
  enterRule(_localctx, 6, BazelBuildParser::RuleArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(45);
    match(BazelBuildParser::ID);
    setState(46);
    match(BazelBuildParser::T__3);
    setState(48);
    value();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ValueContext ------------------------------------------------------------------

BazelBuildParser::ValueContext::ValueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BazelBuildParser::Single_valueContext* BazelBuildParser::ValueContext::single_value() {
  return getRuleContext<BazelBuildParser::Single_valueContext>(0);
}

BazelBuildParser::Multi_valueContext* BazelBuildParser::ValueContext::multi_value() {
  return getRuleContext<BazelBuildParser::Multi_valueContext>(0);
}


size_t BazelBuildParser::ValueContext::getRuleIndex() const {
  return BazelBuildParser::RuleValue;
}

void BazelBuildParser::ValueContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterValue(this);
}

void BazelBuildParser::ValueContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitValue(this);
}


antlrcpp::Any BazelBuildParser::ValueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitValue(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::ValueContext* BazelBuildParser::value() {
  ValueContext *_localctx = _tracker.createInstance<ValueContext>(_ctx, getState());
  enterRule(_localctx, 8, BazelBuildParser::RuleValue);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(52);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BazelBuildParser::StringValue: {
        enterOuterAlt(_localctx, 1);
        setState(50);
        single_value();
        break;
      }

      case BazelBuildParser::T__4: {
        enterOuterAlt(_localctx, 2);
        setState(51);
        multi_value();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Multi_valueContext ------------------------------------------------------------------

BazelBuildParser::Multi_valueContext::Multi_valueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BazelBuildParser::Val_listContext* BazelBuildParser::Multi_valueContext::val_list() {
  return getRuleContext<BazelBuildParser::Val_listContext>(0);
}


size_t BazelBuildParser::Multi_valueContext::getRuleIndex() const {
  return BazelBuildParser::RuleMulti_value;
}

void BazelBuildParser::Multi_valueContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMulti_value(this);
}

void BazelBuildParser::Multi_valueContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMulti_value(this);
}


antlrcpp::Any BazelBuildParser::Multi_valueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitMulti_value(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::Multi_valueContext* BazelBuildParser::multi_value() {
  Multi_valueContext *_localctx = _tracker.createInstance<Multi_valueContext>(_ctx, getState());
  enterRule(_localctx, 10, BazelBuildParser::RuleMulti_value);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(54);
    match(BazelBuildParser::T__4);
    setState(56);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BazelBuildParser::StringValue) {
      setState(55);
      val_list();
    }
    setState(58);
    match(BazelBuildParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Val_listContext ------------------------------------------------------------------

BazelBuildParser::Val_listContext::Val_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BazelBuildParser::Single_valueContext *> BazelBuildParser::Val_listContext::single_value() {
  return getRuleContexts<BazelBuildParser::Single_valueContext>();
}

BazelBuildParser::Single_valueContext* BazelBuildParser::Val_listContext::single_value(size_t i) {
  return getRuleContext<BazelBuildParser::Single_valueContext>(i);
}


size_t BazelBuildParser::Val_listContext::getRuleIndex() const {
  return BazelBuildParser::RuleVal_list;
}

void BazelBuildParser::Val_listContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterVal_list(this);
}

void BazelBuildParser::Val_listContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitVal_list(this);
}


antlrcpp::Any BazelBuildParser::Val_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitVal_list(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::Val_listContext* BazelBuildParser::val_list() {
  Val_listContext *_localctx = _tracker.createInstance<Val_listContext>(_ctx, getState());
  enterRule(_localctx, 12, BazelBuildParser::RuleVal_list);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(60);
    single_value();
    setState(65);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(61);
        match(BazelBuildParser::T__2);
        setState(62);
        single_value(); 
      }
      setState(67);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
    }
    setState(69);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BazelBuildParser::T__2) {
      setState(68);
      match(BazelBuildParser::T__2);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Single_valueContext ------------------------------------------------------------------

BazelBuildParser::Single_valueContext::Single_valueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BazelBuildParser::Single_valueContext::StringValue() {
  return getToken(BazelBuildParser::StringValue, 0);
}


size_t BazelBuildParser::Single_valueContext::getRuleIndex() const {
  return BazelBuildParser::RuleSingle_value;
}

void BazelBuildParser::Single_valueContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterSingle_value(this);
}

void BazelBuildParser::Single_valueContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BazelBuildListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitSingle_value(this);
}


antlrcpp::Any BazelBuildParser::Single_valueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BazelBuildVisitor*>(visitor))
    return parserVisitor->visitSingle_value(this);
  else
    return visitor->visitChildren(this);
}

BazelBuildParser::Single_valueContext* BazelBuildParser::single_value() {
  Single_valueContext *_localctx = _tracker.createInstance<Single_valueContext>(_ctx, getState());
  enterRule(_localctx, 14, BazelBuildParser::RuleSingle_value);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(71);
    match(BazelBuildParser::StringValue);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

// Static vars and initialization.
std::vector<dfa::DFA> BazelBuildParser::_decisionToDFA;
atn::PredictionContextCache BazelBuildParser::_sharedContextCache;

// We own the ATN which in turn owns the ATN states.
atn::ATN BazelBuildParser::_atn;
std::vector<uint16_t> BazelBuildParser::_serializedATN;

std::vector<std::string> BazelBuildParser::_ruleNames = {
  "prog", "stat", "arglist", "argument", "value", "multi_value", "val_list", 
  "single_value"
};

std::vector<std::string> BazelBuildParser::_literalNames = {
  "", "'('", "')'", "','", "'='", "'['", "']'"
};

std::vector<std::string> BazelBuildParser::_symbolicNames = {
  "", "", "", "", "", "", "", "ID", "StringValue", "Whitespace", "Newline", 
  "BlockComment", "LineComment"
};

dfa::Vocabulary BazelBuildParser::_vocabulary(_literalNames, _symbolicNames);

std::vector<std::string> BazelBuildParser::_tokenNames;

BazelBuildParser::Initializer::Initializer() {
	for (size_t i = 0; i < _symbolicNames.size(); ++i) {
		std::string name = _vocabulary.getLiteralName(i);
		if (name.empty()) {
			name = _vocabulary.getSymbolicName(i);
		}

		if (name.empty()) {
			_tokenNames.push_back("<INVALID>");
		} else {
      _tokenNames.push_back(name);
    }
	}

  _serializedATN = {
    0x3, 0x608b, 0xa72a, 0x8133, 0xb9ed, 0x417c, 0x3be7, 0x7786, 0x5964, 
    0x3, 0xe, 0x4c, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4, 0x9, 
    0x4, 0x4, 0x5, 0x9, 0x5, 0x4, 0x6, 0x9, 0x6, 0x4, 0x7, 0x9, 0x7, 0x4, 
    0x8, 0x9, 0x8, 0x4, 0x9, 0x9, 0x9, 0x3, 0x2, 0x7, 0x2, 0x14, 0xa, 0x2, 
    0xc, 0x2, 0xe, 0x2, 0x17, 0xb, 0x2, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x5, 
    0x3, 0x1c, 0xa, 0x3, 0x3, 0x3, 0x3, 0x3, 0x7, 0x3, 0x20, 0xa, 0x3, 0xc, 
    0x3, 0xe, 0x3, 0x23, 0xb, 0x3, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x7, 0x4, 
    0x28, 0xa, 0x4, 0xc, 0x4, 0xe, 0x4, 0x2b, 0xb, 0x4, 0x3, 0x4, 0x5, 0x4, 
    0x2e, 0xa, 0x4, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 
    0x6, 0x3, 0x6, 0x5, 0x6, 0x37, 0xa, 0x6, 0x3, 0x7, 0x3, 0x7, 0x5, 0x7, 
    0x3b, 0xa, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x7, 
    0x8, 0x42, 0xa, 0x8, 0xc, 0x8, 0xe, 0x8, 0x45, 0xb, 0x8, 0x3, 0x8, 0x5, 
    0x8, 0x48, 0xa, 0x8, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x5, 0x21, 0x29, 
    0x43, 0x2, 0xa, 0x2, 0x4, 0x6, 0x8, 0xa, 0xc, 0xe, 0x10, 0x2, 0x2, 0x2, 
    0x4c, 0x2, 0x15, 0x3, 0x2, 0x2, 0x2, 0x4, 0x18, 0x3, 0x2, 0x2, 0x2, 
    0x6, 0x24, 0x3, 0x2, 0x2, 0x2, 0x8, 0x2f, 0x3, 0x2, 0x2, 0x2, 0xa, 0x36, 
    0x3, 0x2, 0x2, 0x2, 0xc, 0x38, 0x3, 0x2, 0x2, 0x2, 0xe, 0x3e, 0x3, 0x2, 
    0x2, 0x2, 0x10, 0x49, 0x3, 0x2, 0x2, 0x2, 0x12, 0x14, 0x5, 0x4, 0x3, 
    0x2, 0x13, 0x12, 0x3, 0x2, 0x2, 0x2, 0x14, 0x17, 0x3, 0x2, 0x2, 0x2, 
    0x15, 0x13, 0x3, 0x2, 0x2, 0x2, 0x15, 0x16, 0x3, 0x2, 0x2, 0x2, 0x16, 
    0x3, 0x3, 0x2, 0x2, 0x2, 0x17, 0x15, 0x3, 0x2, 0x2, 0x2, 0x18, 0x19, 
    0x7, 0x9, 0x2, 0x2, 0x19, 0x1b, 0x7, 0x3, 0x2, 0x2, 0x1a, 0x1c, 0x5, 
    0x6, 0x4, 0x2, 0x1b, 0x1a, 0x3, 0x2, 0x2, 0x2, 0x1b, 0x1c, 0x3, 0x2, 
    0x2, 0x2, 0x1c, 0x1d, 0x3, 0x2, 0x2, 0x2, 0x1d, 0x21, 0x7, 0x4, 0x2, 
    0x2, 0x1e, 0x20, 0x7, 0xc, 0x2, 0x2, 0x1f, 0x1e, 0x3, 0x2, 0x2, 0x2, 
    0x20, 0x23, 0x3, 0x2, 0x2, 0x2, 0x21, 0x22, 0x3, 0x2, 0x2, 0x2, 0x21, 
    0x1f, 0x3, 0x2, 0x2, 0x2, 0x22, 0x5, 0x3, 0x2, 0x2, 0x2, 0x23, 0x21, 
    0x3, 0x2, 0x2, 0x2, 0x24, 0x29, 0x5, 0x8, 0x5, 0x2, 0x25, 0x26, 0x7, 
    0x5, 0x2, 0x2, 0x26, 0x28, 0x5, 0x8, 0x5, 0x2, 0x27, 0x25, 0x3, 0x2, 
    0x2, 0x2, 0x28, 0x2b, 0x3, 0x2, 0x2, 0x2, 0x29, 0x2a, 0x3, 0x2, 0x2, 
    0x2, 0x29, 0x27, 0x3, 0x2, 0x2, 0x2, 0x2a, 0x2d, 0x3, 0x2, 0x2, 0x2, 
    0x2b, 0x29, 0x3, 0x2, 0x2, 0x2, 0x2c, 0x2e, 0x7, 0x5, 0x2, 0x2, 0x2d, 
    0x2c, 0x3, 0x2, 0x2, 0x2, 0x2d, 0x2e, 0x3, 0x2, 0x2, 0x2, 0x2e, 0x7, 
    0x3, 0x2, 0x2, 0x2, 0x2f, 0x30, 0x7, 0x9, 0x2, 0x2, 0x30, 0x31, 0x7, 
    0x6, 0x2, 0x2, 0x31, 0x32, 0x3, 0x2, 0x2, 0x2, 0x32, 0x33, 0x5, 0xa, 
    0x6, 0x2, 0x33, 0x9, 0x3, 0x2, 0x2, 0x2, 0x34, 0x37, 0x5, 0x10, 0x9, 
    0x2, 0x35, 0x37, 0x5, 0xc, 0x7, 0x2, 0x36, 0x34, 0x3, 0x2, 0x2, 0x2, 
    0x36, 0x35, 0x3, 0x2, 0x2, 0x2, 0x37, 0xb, 0x3, 0x2, 0x2, 0x2, 0x38, 
    0x3a, 0x7, 0x7, 0x2, 0x2, 0x39, 0x3b, 0x5, 0xe, 0x8, 0x2, 0x3a, 0x39, 
    0x3, 0x2, 0x2, 0x2, 0x3a, 0x3b, 0x3, 0x2, 0x2, 0x2, 0x3b, 0x3c, 0x3, 
    0x2, 0x2, 0x2, 0x3c, 0x3d, 0x7, 0x8, 0x2, 0x2, 0x3d, 0xd, 0x3, 0x2, 
    0x2, 0x2, 0x3e, 0x43, 0x5, 0x10, 0x9, 0x2, 0x3f, 0x40, 0x7, 0x5, 0x2, 
    0x2, 0x40, 0x42, 0x5, 0x10, 0x9, 0x2, 0x41, 0x3f, 0x3, 0x2, 0x2, 0x2, 
    0x42, 0x45, 0x3, 0x2, 0x2, 0x2, 0x43, 0x44, 0x3, 0x2, 0x2, 0x2, 0x43, 
    0x41, 0x3, 0x2, 0x2, 0x2, 0x44, 0x47, 0x3, 0x2, 0x2, 0x2, 0x45, 0x43, 
    0x3, 0x2, 0x2, 0x2, 0x46, 0x48, 0x7, 0x5, 0x2, 0x2, 0x47, 0x46, 0x3, 
    0x2, 0x2, 0x2, 0x47, 0x48, 0x3, 0x2, 0x2, 0x2, 0x48, 0xf, 0x3, 0x2, 
    0x2, 0x2, 0x49, 0x4a, 0x7, 0xa, 0x2, 0x2, 0x4a, 0x11, 0x3, 0x2, 0x2, 
    0x2, 0xb, 0x15, 0x1b, 0x21, 0x29, 0x2d, 0x36, 0x3a, 0x43, 0x47, 
  };

  atn::ATNDeserializer deserializer;
  _atn = deserializer.deserialize(_serializedATN);

  size_t count = _atn.getNumberOfDecisions();
  _decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    _decisionToDFA.emplace_back(_atn.getDecisionState(i), i);
  }
}

BazelBuildParser::Initializer BazelBuildParser::_init;
