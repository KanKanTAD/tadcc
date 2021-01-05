
#include "Stringify.h"

namespace bazel_base {

string Stringify::stringify() const {
  	sstream ss;
  	this->stringify(ss);
  	return ss.str();
}


} // namespace bazel_base
