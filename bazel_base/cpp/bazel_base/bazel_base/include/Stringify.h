#ifndef BAZEL_BASE_STRINGIFY_H
#define BAZEL_BASE_STRINGIFY_H


#include <string>
using namespace std;

namespace bazel_base {

class Stringify {
  public:
    virtual string stringify() = 0;

};

} // namespace bazel_base
#endif
