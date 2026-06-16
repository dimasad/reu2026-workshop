#include "gtest/gtest.h"
#include "my_cpp_pkg/add_numbers.hpp"

namespace my_cpp_pkg
{

TEST(AddNumbersTest, PositiveNumbers)
{
  EXPECT_EQ(add_numbers(2, 3), 5);
}

TEST(AddNumbersTest, NegativeNumbers)
{
  EXPECT_EQ(add_numbers(-2, -3), -5);
}

TEST(AddNumbersTest, MixedNumbers)
{
  EXPECT_EQ(add_numbers(10, -5), 5);
}

TEST(AddNumbersTest, ZeroNumbers)
{
  EXPECT_EQ(add_numbers(0, 5), 5);
  EXPECT_EQ(add_numbers(5, 0), 5);
  EXPECT_EQ(add_numbers(0, 0), 0);
}

}  // namespace my_cpp_pkg

int main(int argc, char ** argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
