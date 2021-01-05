#ifndef BAZEL_BASE_APPENDEBLE_H
#define BAZEL_BASE_APPENDEBLE_H


namespace bazel_base {

template<class T>
class Appendeble {
  public:
    inline virtual void append(T * obj) = 0;

};

} // namespace bazel_base
#endif
