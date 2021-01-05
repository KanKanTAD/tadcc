#ifndef BAZEL_BASE_MULTIVALUE_H
#define BAZEL_BASE_MULTIVALUE_H


#include "Value.h"
#include <list>
using namespace std;

namespace bazel_base { class SingleValue; } 

namespace bazel_base {

class MultiValue : public Value {
  private:
    list<SingleValue *> values_;

};

} // namespace bazel_base
#endif
