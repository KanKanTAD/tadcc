#ifndef BAZEL_BASE_BAZELBUILD_H
#define BAZEL_BASE_BAZELBUILD_H


#include <list>
using namespace std;
#include "Com.h"

namespace bazel_base { class CallMeta; } 

namespace bazel_base {

class BazelBuild : public Com {
  private:
    list<CallMeta *> call_metis_;

};

} // namespace bazel_base
#endif
