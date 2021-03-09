#pragma once
#include <functional>
#include <future>
namespace tadcc {

class thread_pool {
  size_t pool_size_;

public:
  using TaskType = std::function<void()>;

public:
  explicit thread_pool(size_t pool_size);
  virtual ~thread_pool();

  virtual void emqueue(const TaskType &);
};

template <typename RetType> class task_pool {
  size_t pool_size_;

public:
  using TaskType = std::future<RetType>;

public:
  explicit task_pool(size_t pool_size);
  virtual ~task_pool();
  virtual void emqueue(const TaskType &);
};
} // namespace tadcc

#include "threads_util.tcc"
