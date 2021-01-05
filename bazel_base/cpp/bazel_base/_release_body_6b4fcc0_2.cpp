void ComContext::_release() const {
  // ---- header including this line will be automatically removed ----

  if (obj == nullptr) {
    return;
  }
  _release(obj->get_id());
