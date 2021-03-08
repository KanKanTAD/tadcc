#include <gtest/gtest.h>
#include <tadcc.hpp>

TEST(tadcc, version) {
  auto v = tadcc::version();
  ASSERT_EQ(v.str(), std::string("1.0.0"));
}
int main(int argc, char *argv[]) {
  testing::InitGoogleTest(&argc, argv);

  return RUN_ALL_TESTS();
}
