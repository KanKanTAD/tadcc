
#include "ComContext.h"
#include "Com.h"

namespace bazel_base {

ComContext & ComContext::instance() const
{
}

ComContext::ComContext(){
}

ComContext::~ComContext(){
}

long ComContext::gen_id() const {
return id_inc_.fetch_add(1);
}


} // namespace bazel_base
