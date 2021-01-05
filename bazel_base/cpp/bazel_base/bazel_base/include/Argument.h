#ifndef BAZEL_BASE_ARGUMENT_H
#define BAZEL_BASE_ARGUMENT_H


#include "Com.h"

namespace bazel_base { class Value; } 

namespace bazel_base {

class Argument : public Com {
  private:
    Value * value_=             nullptr;

};

} // namespace bazel_base
#endif
