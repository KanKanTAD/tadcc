#pragma once

#include <mutex>
namespace tadcc {

thread_pool::thread_pool(size_t pool_size) : pool_size_(pool_size) {
  this->work_();
}
thread_pool::~thread_pool() { this->running_ = false; }

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
  this->task_queue_.push_back(task);
}
} // namespace tadcc
