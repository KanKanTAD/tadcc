#include "bazel_base.h"

namespace tadcc {
namespace bazel_base {
Attribute::Attribute(const std::string &name, bool is_multi_)
    : is_multi_(is_multi_) {
  this->name_ = name;
}
Attribute::Attribute(bool is_multi_) : Attribute("", is_multi_) {}

bool Attribute::is_multi() const { return this->is_multi_; }

bool Attribute::add_value(const Value &v) {
  if (this->values_.end() != this->values_.find(v)) {
    return false;
  }
  this->values_.insert(v);
  return true;
}

void Attribute::list_value(const std::list<Value> &result) {
  result.insert(result.end(), this->values_.begin(), this->values_.end());
}

} // namespace bazel_base
} // namespace tadcc
