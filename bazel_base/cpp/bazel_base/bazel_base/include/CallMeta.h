#ifndef BAZEL_BASE_CALLMETA_H
#define BAZEL_BASE_CALLMETA_H


#include <list>
using namespace std;
#include "Com.h"

namespace bazel_base { class Argument; } 

namespace bazel_base {

class CallMeta : public Com {
  private:
    list<Argument *> arguments_;

};

} // namespace bazel_base
#endif
