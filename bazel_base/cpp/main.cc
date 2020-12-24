#include "bazel_base.h"
#include <iostream>
#include <string.h>

using namespace tadcc;
using namespace bazel_base;

int main(int argc, char *argv[]) {
  Value v("hello world");
  std::cout << v << std::endl;
  Value g;
  g = v;
  std::cout << g << std::endl;
  v._delete();
  return 0;
}
