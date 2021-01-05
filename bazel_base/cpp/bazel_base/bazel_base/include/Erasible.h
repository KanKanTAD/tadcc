#ifndef BAZEL_BASE_ERASIBLE_H
#define BAZEL_BASE_ERASIBLE_H


namespace bazel_base {

template<class T>
class Erasible {
  public:
    inline virtual  erase(long id);

    inline virtual  erase(const T & obj);

};
template<class T>
inline  Erasible<T>::erase(long id) {
}

template<class T>
inline  Erasible<T>::erase(const T & obj) {
}


} // namespace bazel_base
#endif
