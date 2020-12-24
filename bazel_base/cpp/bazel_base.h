#pragma once
#include <list>
#include <ostream>
#include <set>
#include <string>

namespace tadcc {
namespace bazel_base {

struct Namiable {
  virtual std::string get_name() const { return this->name_; }
  virtual void set_name(const std::string &name) { this->name_ = name; }

protected:
  std::string name_;
};

struct Value {
  char *value = nullptr;
  int leng = 0;
  Value() {}
  Value(const std::string &);
  Value(const Value &);
  Value(const Value &&);
  std::string str() const;
  virtual ~Value() {}
  virtual void _delete();
  Value operator=(const Value &);
  bool operator==(const Value &);
  bool operator<(const Value &);
};

extern std::ostream &operator<<(std::ostream &, const Value &);

class Attribute : public Namiable {
  std::set<Value> values_;

public:
  virtual ~Attribute();
  Attribute(const std::string &name, bool is_multi_);
  Attribute(bool is_multi_);
  virtual bool is_multi() const;
  virtual void add_value(const Value &);
  virtual void list_value(const std::list<Value> &);
  virtual void remove_value(const Value &);
  virtual void search_value(const std::string &, std::list<Value> &);
  virtual Value find_value(const std::string &);
};

class Target : public Namiable {
public:
  virtual void list_attribute(std::list<Attribute> &attributes);
  virtual std::string get_rulename() const;
  virtual void set_rulename(const std::string &rule_name);
};

class BazelBase : public Namiable {
public:
  virtual void reload(const std::string &file_path);
  virtual void list_target(std::list<Target> &targets);
  virtual void list_target(const std::string rule_name,
                           std::list<Target> &targets);
};
} // namespace bazel_base
} // namespace tadcc
