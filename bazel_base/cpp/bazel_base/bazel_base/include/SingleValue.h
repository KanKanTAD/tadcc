#ifndef BAZEL_BASE_SINGLEVALUE_H
#define BAZEL_BASE_SINGLEVALUE_H


#include "Value.h"
#include <string>
using namespace std;

namespace bazel_base { class Com; } 

namespace bazel_base {

class SingleValue : public Value {
  public:
    explicit SingleValue();

    virtual ~SingleValue();

    virtual string stringify() override;

    inline virtual void erase(long id) override;

    inline virtual void append(Com * obj) override;

};
inline void SingleValue::erase(long id) {
	return;
}

inline void SingleValue::append(Com * obj) {
	return;
}


} // namespace bazel_base
#endif
