#include <string>

#pragma once
namespace tadcc {
namespace ast {

struct TreeNode {
  virtual ~TreeNode();
};

template <typename T> struct ValueNode : public TreeNode { T value; };

struct BinOpNode : public TreeNode {
  std::string op;
  TreeNode *left;
  TreeNode *right;
};

struct PreOpNode : public TreeNode {
  std::string op;
  TreeNode *back;
};

struct SupOpNode : public TreeNode {
  std::string op;
  TreeNode *front;
};
} // namespace ast
} // namespace tadcc
