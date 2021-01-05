#ifndef BAZEL_BASE_MULTIVALUE_H
#define BAZEL_BASE_MULTIVALUE_H


#include "Value.h"
#include "Appendeble.h"
#include <list>
using namespace std;
#include "SingleValue.h"
#include <string>
using namespace std;
#include <iostream>
using namespace std;

namespace bazel_base {

class MultiValue : public Value, public Appendeble<SingleValue> {
  private:
    list<SingleValue*> values_;


  public:
    virtual void append(SingleValue * obj) const override;

    virtual string stringify();

    inline virtual void erase(long id);

    virtual void stringify(ostream out) const;

};
inline void MultiValue::erase(long id) {
}


} // namespace bazel_base
#endif
