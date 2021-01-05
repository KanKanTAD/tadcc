
#include "SingleValue.h"

namespace bazel_base {

SingleValue::SingleValue():SingleValue(""){
}

SingleValue::~SingleValue(){
}

string SingleValue::stringify() {
	return "";
}

void SingleValue::set_value(const string & value) {
	this->value_ = value;
}

SingleValue::SingleValue(const string & value):Value() {
}


} // namespace bazel_base
