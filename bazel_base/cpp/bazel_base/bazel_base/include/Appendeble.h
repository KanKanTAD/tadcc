#ifndef BAZEL_BASE_APPENDEBLE_H
#define BAZEL_BASE_APPENDEBLE_H


namespace bazel_base {

template<class T>
class Appendeble {
  public:
    virtual void append(T * obj) const = 0;

};

} // namespace bazel_base
#endif
