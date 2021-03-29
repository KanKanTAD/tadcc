#include <algorithm>
#include <functional>

namespace tadcc {
namespace bin_tree {

template <typename T> struct bitree {
  T data;
  bitree<T> *parent, *left, *right;
  bitree(const T &d)
      : data(d), parent(nullptr), left(nullptr), right(nullptr) {}
};

template <typename T> inline bitree<T> *grandparent(bitree<T> *node);
template <typename T> inline bitree<T> *sibling(bitree<T> *node);
template <typename T> inline bitree<T> *uncle(bitree<T> *node);
template <typename T> inline bitree<T> *make_head();
template <typename T>
inline bitree<T> *root(bitree<T> *node, bitree<T> *head = nullptr);
template <typename T> void release_all(bitree<T> *root);
template <typename T> int node_count(bitree<T> *node);
template <typename T> int leaf_count(bitree<T> *node);
template <typename T> int hight(bitree<T> *node);
template <typename T> void left_rotate(bitree<T> *node);
template <typename T> void right_rotate(bitree<T> *node);
template <typename T>
void first_view(bitree<T> *node, std::function<void(const T &)> viewer);
template <typename T>
void center_view(bitree<T> *node, std::function<void(const T &)> viewer);
template <typename T>
void last_view(bitree<T> *node, std::function<void(const T &)> viewer);
template <typename T> bitree<T> *far_left(bitree<T> *node);
template <typename T> bitree<T> *far_right(bitree<T> *node);

} // namespace bin_tree
} // namespace tadcc

namespace tadcc {
namespace bin_tree {

template <typename T> inline bitree<T> *make_head() {
  auto h = new bitree<T>({});
  h->left = h->right = h->parent = h;
  return h;
}
template <typename T> inline bitree<T> *grandparent(bitree<T> *node) {
  return node ? (node->parent ? node->parent->parent : nullptr) : nullptr;
}

template <typename T> inline bitree<T> *sibling(bitree<T> *node) {
  return node
             ? (node->parent ? (node == node->parent->left ? node->parent->right
                                                           : node->parent->left)
                             : nullptr)
             : nullptr;
}

template <typename T> inline bitree<T> *uncle(bitree<T> *node) {
  return node ? sibling(node->parent) : nullptr;
}

template <typename T> void release_all(bitree<T> *root) {
  if (!root) {
    return;
  }
  auto left = root->left;
  auto right = root->right;
  delete root;
  release_all(left);
  release_all(right);
}

template <typename T> int hight(bitree<T> *node) {
  if (!node) {
    return 0;
  }
  return 1 + std::max(hight(node->left), hight(node->right));
}

template <typename T> void left_rotate(bitree<T> *node) {
  if (!node) {
    return;
  }
  auto r = node->right;
  if (!r) {
    return;
  }
  node->right = r->left;
  node->right->parent = node;
  r->left = node;
  auto p = node->parent;
  node->parent = r;
  r->parent = p;
  if (!p) {
    return;
  }
  if (p->left == node) {
    p->left = r;
  } else if (p->right == node) {
    p->right = r;
  }
}
template <typename T> void right_rotate(bitree<T> *node) {
  if (!node)
    return;
  auto l = node->left;
  if (!l)
    return;
  node->left = l->right;
  node->left->parent = node;
  l->right = node;
  auto p = node->parent;
  node->parent = l;
  l->parent = p;
  if (!p)
    return;
  if (p->left == node) {
    p->left = l;
  } else if (p->right == node) {
    p->right = l;
  }
}
template <typename T>
void first_view(bitree<T> *node, std::function<void(const T &)> viewer) {
  if (!node) {
    return;
  }
  viewer(node->data);
  first_view(node->left, viewer);
  first_view(node->right, viewer);
}
template <typename T>
void center_view(bitree<T> *node, std::function<void(const T &)> viewer) {
  if (!node) {
    return;
  }
  center_view(node->left, viewer);
  viewer(node->data);
  center_view(node->right, viewer);
}
template <typename T>
void last_view(bitree<T> *node, std::function<void(const T &)> viewer) {
  if (!node) {
    return;
  }
  last_view(node->left, viewer);
  last_view(node->right, viewer);
  viewer(node->data);
}

template <typename T> bitree<T> *far_left(bitree<T> *node) {
  if (node) {
    while (node->left) {
      node = node->left;
    }
  }
  return node;
}
template <typename T> bitree<T> *far_right(bitree<T> *node) {
  if (node) {
    while (node->right) {
      node = node->right;
    }
  }
  return node;
}

template <typename T> int leaf_count(bitree<T> *node) {
  if (!node) {
    return 0;
  }
  if (!node->left && !node->right) {
    return 1;
  }
  return leaf_count(node->left) + leaf_count(node->right);
}
template <typename T> inline bitree<T> *root(bitree<T> *node, bitree<T> *head) {
  while (node && node->parent != head) {
    node = node->parent;
  }
  return node;
}

template <typename T> int node_count(bitree<T> *node) {
  if (!node) {
    return 0;
  }
  return 1 + node_count(node->left) + node_count(node->right);
}

} // namespace bin_tree
} // namespace tadcc
