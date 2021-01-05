
#include "ComContext.h"
#include "Com.h"

namespace bazel_base {

ComContext & ComContext::instance()
{

  static ComContext inst_;
  return inst_;
}

ComContext::ComContext(){
}

ComContext::~ComContext(){
}

long ComContext::gen_id() const {
return id_inc_.fetch_add(1);
}

template<class T>
T * ComContext::make_com() const {
}


} // namespace bazel_base
