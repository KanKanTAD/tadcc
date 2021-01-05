
#include "MultiValue.h"

namespace bazel_base {

void MultiValue::append(SingleValue *obj) const {
  if (obj == nullptr) {
    return;
  }
  obj->father = (Com *)(this);
  this->children.push_back(obj);
}

void MultiValue::stringify(ostream &out) const {
  out << "[";
  bool first = true;
  for (const auto &value : this->children) {
    if (!first)
      cout << ", ";
    first = false;
    value->stringify(out);
  }
  out << "]";
}

} // namespace bazel_base
