#pragma once

#ifdef __linux__
#include <sys/file.h>
#include <unistd.h>
#endif

#include <cassert>
#include <chrono>
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

class flock_guard {
  int fd_;

public:
  flock_guard(const std::string &filepath,
              int lock_type /* LOCK_EX  || LOCK_SH)*/) {
    assert((fd_ = open(filepath.c_str(), O_RDONLY | O_CREAT)) > 0);
    assert(0 == flock(fd_, lock_type));
  }
  virtual ~flock_guard() {
    flock(fd_, LOCK_UN);
    close(fd_);
  }
};

// read lock
class rflock_guard : public flock_guard {
public:
  rflock_guard(const std::string &filepath) : flock_guard(filepath, LOCK_SH) {}
};

// write lock
class wflock_guard : public flock_guard {
public:
  wflock_guard(const std::string &filepath) : flock_guard(filepath, LOCK_EX) {}
};

} // namespace tadcc

namespace tadcc {

thread_pool::thread_pool(size_t pool_size) : pool_size_(pool_size) {
  this->work_();
}
thread_pool::~thread_pool() { this->running_ = false; }

void thread_pool::spin(const time_t t) const {
  while (!this->task_queue_.empty()) {
    std::this_thread::sleep_for(std::chrono::microseconds(t));
  }
}

void thread_pool::work_() {
  for (int i = 0; i < pool_size_; ++i) {
    this->workers_.emplace_back([this]() {
      while (this->running_) {
        TaskType task;
        {
          std::unique_lock<std::mutex> lk_(this->queue_mutex_);
          this->condition_.wait(lk_, [this]() {
            return !this->running_ || !this->task_queue_.empty();
          });
          task = this->task_queue_.front();
          if (!this->running_) {
            return;
          }
          this->task_queue_.pop();
        }
        task();
      }
    });
  }
}

void thread_pool::emqueue(const TaskType &task) {
  std::lock_guard<std::mutex> lk_(this->queue_mutex_);
  this->task_queue_.push(task);
}
} // namespace tadcc
