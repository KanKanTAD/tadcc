#include "BazelBuild.h"
#include "ComContext.h"
#include "SingleValue.h"

#include <cassert>
#include <exception>
#include <iostream>
#include <set>

#define Run_Test(func_name)                                                    \
  try {                                                                        \
    func_name();                                                               \
  } catch (std::exception & e) {                                               \
    std::cout << e.what() << std::endl;                                        \
  }

void test_gen_obj() {
  int i = 100;
  while (i--) {
    auto value =
        bazel_base::ComContext::instance().make_com<bazel_base::SingleValue>();
    std::cout << value->get_id() << std::endl;
  }
}

void test_gen_id() {
  std::set<long> id_s;
  int c = 100;
  for (int i = 0; i < c; i++) {
    id_s.insert(bazel_base::ComContext::instance().gen_id());
  }
  assert(id_s.size() == c);
}

int main(int argc, char *argv[]) {
  Run_Test(test_gen_id);
  Run_Test(test_gen_obj);
  return 0;
}
