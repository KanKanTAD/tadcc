#include <fstream>
#include <iostream>
#include <istream>
#include <string>
using namespace std;

enum State { sAll, sNewLine, sWord };

static int lines = 0;
static int chars = 0;
static int words = 0;

class StateMache {
  istream &ist_;

public:
  StateMache(istream &ist) : ist_(ist) {}
  virtual ~StateMache() {}
  bool next_state(State &s) {
    char c;

    while (ist_ >> c) {
      if (c == '\n') {
        s = State::sNewLine;
        return true;
      } else if ()
    }
    return false;
  }
};

class Lexer {
  StateMache &mache_;

public:
  Lexer(StateMache &mache) : mache_(mache) {}
  virtual ~Lexer() {}
  void run() {
    State s;
    while (mache_.next_state(s)) {
      switch (s) {
      case sWord:
        break;
      case sNewLine:
        break;
      case sAll:
        break;
      }
    }
  }
};
int main(int argc, char *args[]) {

  fstream fs;
  istream *ist = nullptr;
  if (argc > 1) {
    fs.open(args[1]);
    ist = &fs;
  } else {
    ist = &cin;
  }
  StateMache mache(*ist);
  Lexer lex(mache);
  lex.run();

  return 0;
}
