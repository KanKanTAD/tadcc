#ifndef BAZEL_BASE_TREIFY_H
#define BAZEL_BASE_TREIFY_H


#include <list>
using namespace std;

namespace bazel_base {

template<class >
struct Treify {
    Treify<> * father = nullptr;

    list<Treify<> *> children;

};

} // namespace bazel_base
#endif
