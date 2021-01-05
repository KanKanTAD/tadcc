
#include "Stringify.h"
#include <sstream>

namespace bazel_base {

string Stringify::stringify() const {
  std::stringstream ss;
  this->stringify(ss);
  return ss.str();
}

} // namespace bazel_base
