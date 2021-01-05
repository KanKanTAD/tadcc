#ifndef BAZEL_BASE_VALUE_H
#define BAZEL_BASE_VALUE_H


#include "Com.h"

namespace bazel_base {

class Value : public Com {
  public:
    explicit Value();

    virtual ~Value();

};

} // namespace bazel_base
#endif
