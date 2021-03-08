#pragma once

#include <string>
#include <vector>

namespace tadcc {

void str_upper(std::string &s);
void str_upper(const std::string &s, std::string &result);
std::string str_upper(const std::string &s);

void str_lower(std::string &s);
void str_lower(const std::string &s, std::string &result);
std::string str_lower(const std::string &s);

void trim(std::string &cont__, const std::string &s = " \t\r\n");
void rtrim(std::string &cont__, const std::string &s = " \t\r\n");
void ltrim(std::string &cont__, const std::string &s = " \t\r\n");

std::string strip(const std::string &cont__, const std::string &s = " \t\r\n");
std::string rstrip(const std::string &cont__, const std::string &s = " \t\r\n");
std::string lstrip(const std::string &cont__, const std::string &s = " \t\r\n");

void pattern_split(const std::string &master__, const std::string &pattern,
                   std::vector<std::string> &result);
void str_split(const std::string &master__, const std::string &seq,
               std::vector<std::string> &result);
void char_split(const std::string &master__, const std::string &seq,
                std::vector<std::string> &result);

template <typename Ty>
void str_join(const std::string &seq, const std::vector<Ty> &vk,
              std::string &result);
template <typename IterTy>
void str_join(const std::string &seq, const IterTy &beg__, const IterTy &end__,
              std::string &result);

bool str_equals(const std::string &a, const std::string &b);
} // namespace tadcc

#include "string_alg.tcc"
