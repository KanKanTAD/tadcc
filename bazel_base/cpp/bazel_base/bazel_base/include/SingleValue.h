#ifndef BAZEL_BASE_SINGLEVALUE_H
#define BAZEL_BASE_SINGLEVALUE_H


#include "Value.h"

namespace bazel_base {

class SingleValue : public Value {
  public:
    explicit SingleValue();

    virtual ~SingleValue();

};

} // namespace bazel_base
#endif
