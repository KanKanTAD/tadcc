#ifndef BAZEL_BASE_IDENTIFY_H
#define BAZEL_BASE_IDENTIFY_H

#include <ComContext.h>

namespace bazel_base {

class Identify {
public:
  virtual long get_id() const;

private:
  long id_ = 0L;

public:
  explicit Identify();

  virtual ~Identify();
};

} // namespace bazel_base
#endif
