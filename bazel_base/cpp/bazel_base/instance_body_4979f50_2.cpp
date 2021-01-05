ComContext & ComContext::instance() const
{
// ---- header including this line will be automatically removed ----

  static ComContext inst_;
  return inst_;
