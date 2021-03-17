#pragma once

namespace tadcc {
namespace nmc {

long gcd(long a, long b);
long lcm(long a, long b);

} // namespace nmc

} // namespace tadcc

namespace tadcc {
namespace nmc {

long gcd(long a, long b) {
  if (b <= 0) {
    return a;
  }
  return a > b ? gcd(b, a % b) : gcd(a, b % a);
}

long lcm(long a, long b) { return a * b / gcd(a, b); }

} // namespace nmc

} // namespace tadcc
