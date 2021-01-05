#ifndef BAZEL_BASE_NAMIABLE_H
#define BAZEL_BASE_NAMIABLE_H


#include <string>
using namespace std;

namespace bazel_base {

class Namiable {
  public:
    virtual void set_name(const string & name);

    virtual string get_name() const;


  private:
    string name_;

};

} // namespace bazel_base
#endif
