
#include "Identify.h"
#include "ComContext.h"

namespace bazel_base {

long Identify::get_id() const {
 return this->id_;
}

Identify::Identify(){
 this->id_ = ComContext::instance().gen_id();
}

Identify::~Identify(){
}


} // namespace bazel_base
