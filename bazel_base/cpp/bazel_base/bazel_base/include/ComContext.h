#ifndef BAZEL_BASE_COMCONTEXT_H
#define BAZEL_BASE_COMCONTEXT_H


#include <map>
using namespace std;
#include <atomic>
using namespace std;

namespace bazel_base { class Com; } 

namespace bazel_base {

class ComContext {
  public:
    static ComContext & instance();


  private:
    explicit ComContext();


  public:
    virtual ~ComContext();


  private:
    ComContext(ComContext & source);

    ComContext(const ComContext & source);

    ComContext & operator =(ComContext & source) = delete;

    ComContext & operator =(const ComContext & source) = delete;


  public:
    virtual long gen_id() const;

    template<class T>
    inline T * make_com() const {
                            auto o = new T;
                            this->con_.insert(std::make_pair(o->get_id(), (Com *)o));
                            return o;
                          };

    void _release(long id) const;

    void _release(Com * obj) const;


  private:
    mutable map<long,Com*> con_;

    mutable atomic_long id_inc_;

};

} // namespace bazel_base
#endif
