#pragma once
#include <list>
#include <ostream>
#include <set>
#include <string>

namespace tadcc {
namespace bazel_base {

struct Namiable {
  virtual const std::string &get_name() const { return this->name_; }
  virtual void set_name(const std::string &name) { this->name_ = name; }

protected:
  std::string name_;
};

struct Notiable {
  virtual const std::string &get_note() const { return note_; }
  virtual void set_node(const std::string &node) { this->note_ = node; }

protected:
  std::string note_;
};

struct Value : public Notiable {
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

class Attribute : public Namiable, public Notiable {
  std::set<Value> values_;
  bool is_multi_;

public:
  Attribute(const std::string &name, bool is_multi_);
  Attribute(bool is_multi_);
  virtual ~Attribute();
  virtual bool is_multi() const;
  virtual bool add_value(const Value &);
  virtual void list_value(const std::list<Value> &);
  virtual void remove_value(const Value &);
  virtual void search_value(const std::string &, std::list<Value> &);
  virtual Value find_value(const std::string &) const;
};

class Target : public Namiable, public Notiable {
public:
  virtual void list_attribute(std::list<Attribute> &attributes) const;
  virtual std::string get_rulename() const;
  virtual void set_rulename(const std::string &rule_name);
  virtual Attribute &select_attr(const std::string &attr_name);
};

class BazelBase : public Namiable ,public Notiable{
public:
  virtual void reload(const std::string &file_path);
  virtual void list_target(std::list<Target> &targets);
  virtual void list_target(const std::string rule_name,
                           std::list<Target> &targets);
};
} // namespace bazel_base
} // namespace tadcc
