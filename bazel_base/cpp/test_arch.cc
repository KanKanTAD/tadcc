#include "BazelBuild.h"
#include "ComContext.h"
#include <cassert>
#include <exception>
#include <iostream>
#include <set>

void test_gen_id() {
  std::set<long> id_s;
  int c = 100;
  for (int i = 0; i < c; i++) {
    id_s.insert(bazel_base::ComContext::instance().gen_id());
  }
  assert(id_s.size() == c);
}
int main(int argc, char *argv[]) {

  try {
    test_gen_id();
  } catch (std::exception &e) {
    std::cout << e.what() << std::endl;
  }

  return 0;
}
