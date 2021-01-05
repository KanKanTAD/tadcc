#ifndef BAZEL_BASE_TREIFY_H
#define BAZEL_BASE_TREIFY_H

#include <list>
using namespace std;

namespace bazel_base {

template <class T> struct Treify {
  mutable T *father = nullptr;

  mutable list<T *> children;
};

} // namespace bazel_base
#endif
