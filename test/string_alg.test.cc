#include <cstdio>
#include <gtest/gtest.h>
#include <gtest/internal/gtest-port.h>
#include "tadcc.hpp"

TEST(string_alg, trim) {
  std::string s = "  abc\t  ";
  std::string s0 = "abc";
  tadcc::trim(s);
  ASSERT_EQ(s, s0);
}

TEST(string_alg, str_join) {
  std::string result;
  tadcc::str_join<int>(",", {1, 2, 3, 4}, result);
  ASSERT_EQ(result, "1,2,3,4");
}

TEST(string_alg, case_upper) {
  std::string x = "AbcdEfg";
  std::string y = "ABCDEFG";
  std::string z = "abcdefg";
  // ASSERT_EQ(tadcc::strUpper(x), y);
  // ASSERT_EQ(tadcc::strLower(x), z);
}

int main(int argc, char *argv[]) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
