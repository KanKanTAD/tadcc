#include "bazel_base.h"
#include <string>

namespace tadcc {
namespace bazel_base {
namespace bazel_ast {
struct TreeNode {
  virtual ~TreeNode();
};

class Tokenor {
public:
  virtual void begin();
  virtual void end();
};

class Lexer {
public:
  virtual bool match_symbol(std::string &);
  virtual bool match_strval(std::string &);
};

class Parser {
public:
  virtual bool start_parser(BazelBase &result);
};

} // namespace bazel_ast
} // namespace bazel_base
} // namespace tadcc
