#pragma once
#include <sstream>
#include <string>

namespace tadcc {
struct Version_t {
  long major;
  long midden;
  long mijor;
  std::string str() const {
    std::stringstream ss;
    ss << major << "." << midden << "." << mijor;
    return ss.str();
  }
};

const Version_t version() { return {1, 0, 0}; }
} // namespace tadcc
