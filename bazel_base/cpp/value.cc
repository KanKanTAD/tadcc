#include "bazel_base.h"
#include <string.h>

namespace tadcc {
namespace bazel_base {

Value::Value(const Value &&other) {
  this->value = other.value;
  this->leng = other.leng;
}

Value::Value(const Value &other) : Value(std::move(other)) {}

Value::Value(const std::string &s) {
  this->leng = s.size() + 1;
  this->value = new char[this->leng];
  strcpy(this->value, s.c_str());
}

void Value::_delete() {
  delete[] this->value;
  this->value = nullptr;
  this->leng = 0;
}
std::string Value::str() const {
  if (this->value == nullptr) {
    return "";
  }
  return std::string(this->value);
}
bool Value::operator==(const Value &other) {
  return (this->leng == other.leng) && (this->str() == other.str());
}

bool Value::operator<(const Value &other) { return this->str() < other.str(); }

Value Value::operator=(const Value &other) {
  this->value = other.value;
  this->leng = other.leng;
  return *this;
}

std::ostream &operator<<(std::ostream &out, const Value &self) {
  if (self.value != nullptr)
    out << self.value;
  return out;
}

} // namespace bazel_base
} // namespace tadcc
