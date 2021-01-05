
#include "Namiable.h"

namespace bazel_base {

void Namiable::set_name(const string & name) {
this->name_ = name
}

string Namiable::get_name() const {
	return this->name_;
}


} // namespace bazel_base
