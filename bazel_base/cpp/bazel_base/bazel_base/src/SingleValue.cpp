
#include "SingleValue.h"

namespace bazel_base {

SingleValue::SingleValue():SingleValue(""){
}

SingleValue::~SingleValue(){
}

void SingleValue::set_value(const string & value) {
	this->value_ = value;
}

SingleValue::SingleValue(const string & value):Value() {
}

void SingleValue::stringify(ostream out) const {
}


} // namespace bazel_base
