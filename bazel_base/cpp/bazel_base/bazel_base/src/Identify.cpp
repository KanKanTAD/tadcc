
#include "Identify.h"

namespace bazel_base {

long Identify::get_id() const {
}

Identify::Identify(){
 this->id_ = ComContext::instance().gen_id();
}

Identify::~Identify(){
}


} // namespace bazel_base
