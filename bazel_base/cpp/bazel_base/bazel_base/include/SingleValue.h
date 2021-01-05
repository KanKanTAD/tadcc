#ifndef BAZEL_BASE_SINGLEVALUE_H
#define BAZEL_BASE_SINGLEVALUE_H


#include "Value.h"
#include <string>
using namespace std;

namespace bazel_base {

class SingleValue : public Value {
  public:
    explicit SingleValue();

    virtual ~SingleValue();

    virtual string stringify();

    inline virtual void erase(long id);

    inline virtual void append(T * obj);

};
inline void SingleValue::erase(long id) {
}

inline void SingleValue::append(T * obj) {
}


} // namespace bazel_base
#endif
