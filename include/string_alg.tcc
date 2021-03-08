#pragma once

#include <algorithm>
#include <regex>

namespace tadcc {

static inline bool chr_in_str(char c, const std::string &s) {
  return s.find(c) != s.npos;
}

void trim(std::string &cont__, const std::string &s) {
  rtrim(cont__, s);
  ltrim(cont__, s);
}

void rtrim(std::string &cont__, const std::string &s) {
  while (!cont__.empty()) {
    if (chr_in_str(cont__.back(), s)) {
      cont__.pop_back();
    } else {
      break;
    }
  }
}

void ltrim(std::string &cont__, const std::string &s) {
  std::reverse(cont__.begin(), cont__.end());
  rtrim(cont__, s);
  std::reverse(cont__.begin(), cont__.end());
}

std::string strip(const std::string &cont__, const std::string &s) {
  auto res = cont__;
  trim(res);
  return res;
}

std::string rstrip(const std::string &cont__, const std::string &s) {
  auto res = cont__;
  rtrim(res);
  return res;
}

std::string lstrip(const std::string &cont__, const std::string &s) {
  auto res = cont__;
  ltrim(res);
  return res;
}

void pattern_split(const std::string &master__, const std::string &pattern,
                   std::vector<std::string> &result) {
  std::regex r(pattern);
  result = std::vector<std::string>(
      std::sregex_token_iterator(master__.begin(), master__.end(), r, -1),
      std::sregex_token_iterator());
}
void str_split(const std::string &master__, const std::string &seq,
               std::vector<std::string> &result) {
  result.clear();
  size_t pos = 0;
  size_t nxt_pos = 0;
  while (pos < master__.size() &&
         (nxt_pos = master__.find(seq, pos)) != master__.npos) {
    result.push_back(master__.substr(pos, nxt_pos - pos));
    pos = nxt_pos + seq.size();
  }
}

static inline size_t find_CharSet(const std::string &master__,
                                  const std::string &charSet__,
                                  const size_t pos = 0) {
  for (auto p = pos; p < master__.size(); ++p) {
    if (chr_in_str(master__.at(p), charSet__)) {
      return p;
    }
  }
  return master__.npos;
}
void char_split(const std::string &master__, const std::string &seq,
                std::vector<std::string> &result) {
  result.clear();
  size_t pos = 0;
  size_t nxt_pos = 0;
  while (pos < master__.size() &&
         (nxt_pos = find_CharSet(master__, seq, pos)) != master__.npos) {
    result.push_back(master__.substr(pos, nxt_pos - pos));
    pos = nxt_pos + seq.size();
  }
}

template <typename IterTy>
void str_join(const std::string &seq, const IterTy &beg__, const IterTy &end__,
              std::string &result) {

  std::stringstream ss;
  bool is_first = true;
  for (auto it = beg__; it != end__; it++) {
    if (it != beg__) {
      ss << seq;
    }
    ss << *it;
  }
  result = ss.str();
}

template <typename Ty>
void str_join(const std::string &seq, const std::vector<Ty> &vk,
              std::string &result) {

  str_join(seq, vk.begin(), vk.end(), result);
}

void str_upper(std::string &s) {
  for (auto &c : s) {
    c = std::toupper(c);
  }
}

void str_upper(const std::string &s, std::string &result) {
  result = s;
  str_upper(result);
}

std::string str_upper(const std::string &s) {
  auto res = s;
  str_upper(res);
  return res;
}

} // namespace tadcc
