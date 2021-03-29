namespace tadcc {
namespace cybernetics {

template <typename Tp> class Kalman {
  Tp e_est_;
  Tp e_mea_;
  Tp x_k_;

public:
  Kalman(Tp x, Tp e_est, Tp e_mea) : x_k_(x), e_est_(e_est), e_mea_(e_mea) {}

  Tp update(Tp z) {
    auto k_k = e_est_ / (e_est_ + e_mea_);
    x_k_ = x_k_ + k_k * (z - x_k_);
    e_est_ = (1.0f - k_k) * e_est_;
    e_mea_ = (e_mea_ + e_est_) * 0.5f;
    return x_k_;
  }

  Tp x() const { return x_k_; }
};

using Kalman_float = Kalman<float>;

} // namespace cybernetics
} // namespace tadcc
