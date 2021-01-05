#ifndef BAZEL_BASE_COM_H
#define BAZEL_BASE_COM_H


#include "Stringify.h"
#include "Namiable.h"
#include "Identify.h"
#include "Removible.h"
#include "Treify.h"
#include "Erasible.h"

namespace bazel_base {

class Com : public Stringify, public Namiable, public Identify, public Removible, public Treify<Com>, public Erasible<Com> {
  public:
    virtual ~Com();

    explicit Com();

};

} // namespace bazel_base
#endif
