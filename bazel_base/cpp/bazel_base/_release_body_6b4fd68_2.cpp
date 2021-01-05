void ComContext::_release(long id) const {
// ---- header including this line will be automatically removed ----

  auto it = this->con_.find(id);
  if (it == this->con_.end()) {
    return;
  }
  delete it->second;
  this->con_.erase(it);
