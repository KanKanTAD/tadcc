#include "tadcc.hpp"
#include <iostream>

void test_thread_pool() {
  tadcc::thread_pool pool(3);
  std::function<void()> fc_ = []() {
    auto pid = std::this_thread::get_id();
    for (int i = 0; i < 100; i++) {
      std::cout << "pid:" << pid << ":" << i << std::endl;
    }
  };
  for (int i = 0; i = 100; i++) {
    pool.emqueue(fc_);
  }
  pool.spin();
}
int main() {
  test_thread_pool();
  return 0;
}
