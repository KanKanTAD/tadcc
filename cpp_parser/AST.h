#include <string>
using namespace std;
namespace tadcc {

struct TreeNode {
  virtual ~TreeNode();
};

struct NameNode : public TreeNode {
  string name;
};

struct SymbolNode : public TreeNode {
  string pre;
  SymbolNode *fix;
};
template <typename T> struct ValueNode : public TreeNode { T value; };

struct BinOpNode : public TreeNode {
  string op;
  TreeNode *left;
  TreeNode *right;
  virtual ~BinOpNode();
};

struct PreOpNode : public TreeNode {
  string op;
  TreeNode *fix;
  virtual ~PreOpNode();
};

} // namespace tadcc
