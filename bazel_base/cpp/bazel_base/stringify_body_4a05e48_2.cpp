string Stringify::stringify() const {
  // ---- header including this line will be automatically removed ----
	sstream ss;
	this->stringify(ss);
	return ss.str();