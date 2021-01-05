template<class T>
inline void Erasible<T>::erase(T * obj) {
// ---- header including this line will be automatically removed ----
  	if(obj == nullptr){return;}
  	this->erase(obj->get_id());
