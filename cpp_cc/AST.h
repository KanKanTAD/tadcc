#pragma once
namespace tadcc {
namespace ast {

struct TreeNode {
  virtual ~TreeNode();
};

template <typename T> struct ValueNode { T value; };
} // namespace ast
} // namespace tadcc
