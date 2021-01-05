#ifndef BAZEL_BASE_STRINGIFY_H
#define BAZEL_BASE_STRINGIFY_H

#include <iostream>
#include <string>
using namespace std;

namespace bazel_base {

class Stringify {
public:
  virtual string stringify() const;

  virtual void stringify(ostream &out) const = 0;
};

} // namespace bazel_base
#endif
