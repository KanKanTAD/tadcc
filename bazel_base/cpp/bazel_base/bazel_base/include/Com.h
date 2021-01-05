#ifndef BAZEL_BASE_COM_H
#define BAZEL_BASE_COM_H

#include "Erasible.h"
#include "Identify.h"
#include "Namiable.h"
#include "Removible.h"
#include "Stringify.h"
#include "Treify.h"

namespace bazel_base {

class Com : public Stringify,
            public Namiable,
            public Identify,
            public Removible,
            public Treify<Com>,
            public Erasible<Com>,
            public Appendeble<Com> {
public:
  virtual ~Com();
};

} // namespace bazel_base
#endif
