#ifndef BAZEL_BASE_ERASIBLE_H
#define BAZEL_BASE_ERASIBLE_H


namespace bazel_base {

template<class T>
class Erasible {
  public:
    inline virtual void erase(long id) = 0;

    inline virtual void erase(T * obj);

};
template<class T>
inline void Erasible<T>::erase(T * obj) {
  	if(obj == nullptr){return;}
  	this->earse(obj.get_id());
}


} // namespace bazel_base
#endif
