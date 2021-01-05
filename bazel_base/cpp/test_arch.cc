#include "BazelBuild.h"
#include "ComContext.h"
#include "MultiValue.h"
#include "SingleValue.h"

#include <exception>
#include <iostream>
#include <set>
#include <string>

#define Assert(expr)                                                           \
  {                                                                            \
    if ((expr) == false) {                                                     \
      std::string estr = "error hapend in ";                                   \
      estr += __func__;                                                        \
      estr += ":";                                                             \
      estr += std::to_string(__LINE__);                                        \
      throw std::bad_exception();                                              \
    }                                                                          \
  }
;

#define Run_Test(func_name)                                                    \
  try {                                                                        \
    func_name();                                                               \
  } catch (std::exception & e) {                                               \
    std::cout << e.what() << std::endl;                                        \
  };

void test_multi_value_show() {

  auto m_value =
      bazel_base::ComContext::instance().make_com<bazel_base::MultiValue>();
  for (int i = 0; i < 10; i++) {
    auto obj =
        bazel_base::ComContext::instance().make_com<bazel_base::SingleValue>();
    obj->set_value(std::to_string(i) + "kk");
    m_value->append(obj);
  }
  m_value->stringify(std::cout);
}
void test_gen_obj() {
  int i = 100;
  while (i--) {
    auto value =
        bazel_base::ComContext::instance().make_com<bazel_base::SingleValue>();
    // std::cout << value->get_id() << std::endl;
  }
  Assert(false);
}

void test_gen_id() {
  std::set<long> id_s;
  int c = 100;
  for (int i = 0; i < c; i++) {
    id_s.insert(bazel_base::ComContext::instance().gen_id());
  }
  Assert(id_s.size() == c);
}

int main(int argc, char *argv[]) {
  Run_Test(test_gen_id);
  Run_Test(test_gen_obj);
  Run_Test(test_multi_value_show);
  return 0;
}
