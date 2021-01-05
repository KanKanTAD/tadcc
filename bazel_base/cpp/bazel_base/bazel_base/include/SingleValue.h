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

    virtual string stringify() override;

    inline virtual void erase(long id) override;

    virtual void set_value(const string & value);


  private:
    string value_;


  public:
    SingleValue(const string & value);

};
inline void SingleValue::erase(long id) {
	return;
}


} // namespace bazel_base
#endif
