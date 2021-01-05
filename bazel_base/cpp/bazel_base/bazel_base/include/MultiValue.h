#ifndef BAZEL_BASE_MULTIVALUE_H
#define BAZEL_BASE_MULTIVALUE_H

#include "Appendeble.h"
#include "SingleValue.h"
#include "Value.h"
#include <iostream>
#include <list>
#include <string>
using namespace std;

namespace bazel_base {

class MultiValue : public Value, public Appendeble<SingleValue> {
private:
  mutable list<SingleValue *> values_;

public:
  virtual void append(SingleValue *obj) const override;

  inline virtual void erase(long id);

  virtual void stringify(ostream &out) const override;
};
inline void MultiValue::erase(long id) {}

} // namespace bazel_base
#endif
