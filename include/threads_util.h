#pragma once
#include <condition_variable>
#include <functional>
#include <future>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

namespace tadcc {

class thread_pool {

public:
  using TaskType = std::function<void()>;

public:
  explicit thread_pool(size_t pool_size = 16);
  virtual ~thread_pool();

  virtual void emqueue(const TaskType &);
  virtual void spin(const time_t t = 20) const;
  // virtual void clear();
  // virtual void join();

private:
  void work_();

private:
  bool running_ = true;
  size_t pool_size_;
  std::vector<std::thread> workers_;
  std::queue<TaskType> task_queue_;
  std::mutex queue_mutex_;
  std::condition_variable condition_;
};

/**
template <typename RetType> class task_pool {
  size_t pool_size_;

public:
  using TaskType = std::future<RetType>;

public:
  explicit task_pool(size_t pool_size);
  virtual ~task_pool();
  virtual void emqueue(const TaskType &);
};
**/

} // namespace tadcc

#include "threads_util.tcc"
