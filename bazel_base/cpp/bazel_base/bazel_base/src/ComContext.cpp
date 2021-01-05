
#include "ComContext.h"
#include "Com.h"

namespace bazel_base {

ComContext &ComContext::instance() {

  static ComContext inst_;
  return inst_;
}

ComContext::ComContext() {}

ComContext::~ComContext() {

  for (auto [id, obj] : this->con_) {
    delete obj;
  }
  this->con_.clear();
}

long ComContext::gen_id() const { return id_inc_.fetch_add(1); }

template <class T> T *ComContext::make_com() const {

  auto o = new T();
  this->con_.insert({o->get_id(), o});
  return o;
}

void ComContext::_release(long id) const {

  auto it = this->con_.find(id);
  if (it == this->con_.end()) {
    return;
  }
  delete it->second;
  this->con_.erase(it);
}

void ComContext::_release(Com *obj) const {

  if (obj == nullptr) {
    return;
  }
  _release(obj->get_id());
}

} // namespace bazel_base
