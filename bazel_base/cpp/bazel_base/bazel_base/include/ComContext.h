#ifndef BAZEL_BASE_COMCONTEXT_H
#define BAZEL_BASE_COMCONTEXT_H


namespace bazel_base { class Com; } 

namespace bazel_base {

class ComContext {
  public:
    static ComContext& get_instance() const;


  private:
    explicit ComContext();


  public:
    virtual ~ComContext();


  private:
    ComContext(ComContext & source);

    ComContext(const ComContext & source);

    ComContext & operator=(ComContext & source) = delete;

    ComContext & operator=(const ComContext & source) = delete;

};

} // namespace bazel_base
#endif
