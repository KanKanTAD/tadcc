#pragma once
#include <string>

/**
 * head
 */
namespace tadcc {
inline namespace net {
class TCPSocket {
public:
  TCPSocket(const std::string &, const unsigned long);
};
} // namespace net
} // namespace tadcc

/**
 * body
 */
namespace tadcc {
inline namespace net {}
} // namespace tadcc
