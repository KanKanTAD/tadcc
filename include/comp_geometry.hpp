/**
comp_geometry.hpp
**/

#include <cmath>
#include <iostream>

namespace cgeo
{

constexpr double pi = 3.1415926;
constexpr double pi2 = pi / 2;

inline constexpr int sign(const double x,const double eps = 1e-10)
{
    if(std::abs(x) < eps) return 0;
    if (x > 0) return 1;
    return -1;
}

template<typename T>
inline constexpr int sign(const T x)
{
    if (x == 0) return 0;
    if (x > 0) return 1;
    return -1;
}

}

/* interface */
namespace cgeo
{
inline namespace interface
{
#define interface struct

template<typename T>
interface weightable
{
    virtual T _w(const int idx) const = 0;
};

template<typename Res>
interface Dot_able : virtual public weightable<Res>
{
    virtual Res dot(const Dot_able<Res>& a) const = 0;
};

template<typename Res>
interface Det_able : virtual public weightable<Res>
{
    virtual Res det(const Det_able<Res>& a) const = 0;
};

template<typename Res>
interface Dist_able : virtual public weightable<Res>
{
    virtual Res dist(const Dist_able<Res>& a) const = 0;
};

#undef interface

}

template<typename Res>
Res dot(const Dot_able<Res>& a, const Dot_able<Res>& b)
{
    return a.dot(b);
}

template<typename Res>
Res det(const Det_able<Res>& a, const Det_able<Res>& b)
{
    return a.det(b);
}

template<typename Res>
Res dist(const Dist_able<Res>& a, const Dist_able<Res>& b)
{
    return a.dist(b);
}

}


/* point2 */
namespace cgeo
{
template<typename T>
struct point2 : virtual public
    interface::Dot_able<T>,
    interface::Det_able<T>,
    interface::Dist_able<T>
{
    T x;
    T y;
    point2(const T x,const T y):x(x),y(y) {}
    point2():point2(0,0) {}

    virtual void input()
    {
        std::cin >> this->x;
        std::cin >> this->y;
    }

    virtual T norm() const
    {
        return std::sqrt(this->x * this->x  +  this->y * this->y);
    }

    T _w(const int idx) const override
    {
        switch(idx)
        {
        case 0:
            return this->x;
        case 1:
            return this->y;
        default:
            break;
        }
        return this->x;
    }

    T dot(const Dot_able<T>& a) const override
    {
        return this->_w(0) * a._w(0) + this->_w(1) * a._w(1);
    }

    T det(const Det_able<T>& a) const override
    {
        return this->_w(0) * a._w(1) - this->_w(1) * a._w(0);
    }

    T dist(const Dist_able<T>& a) const override
    {
        return T(std::sqrt(std::pow((this->_w(0) - a._w(0)), 2) + std::pow((this->_w(1) - a._w(1)), 2)));
    }

    auto rotate(const double A) const
    {
        return point2<T> {this->x * std::cos(A) - this->y * std::sin(A),
                          this->x * std::sin(A) + this->y * std::cos(A)
                         };
    }

    friend std::ostream& operator << (std::ostream& out, const point2<T>& p)
    {
        out << "Point:["<<p.x<<", " << p.y <<"]";
    }

    friend point2<T> operator == (const point2<T>& a, const point2<T>& b)
    {
        return (cgeo::sign(a.x - b.x) == 0) && (cgeo::sign(a.y - b.y) == 0);
    }

    friend point2<T> operator != (const point2<T>& a, const point2<T>& b)
    {
        return !(a == b);
    }

    friend point2<T> operator + (const point2<T>& a, const point2<T>& b)
    {
        return point2<T> {a.x + b.x, a.y + b.y};
    }

    friend point2<T> operator - (const point2<T>& a, const point2<T>& b)
    {
        return point2<T> {a.x - b.x, a.y - b.y};
    }

    friend point2<T> operator * (const point2<T>& a, const T C)
    {
        return point2<T> {a.x * C, a.y * C};
    }

    friend point2<T> operator * (const T C, const point2<T>& a)
    {
        return (a * C);
    }

    friend point2<T> operator / (const point2<T>& a, const T C)
    {
        return point2<T> {a.x / C, a.y / C};
    }
};


using point2d = point2<double>;

}

/* line2 */
namespace cgeo
{

template<typename T>
struct line2
{
    point2<T> a;
    point2<T> b;
    point2() = default;
    point2(const point2<T>& a,const point2<T>& b):a(a),b(b) {}
    explicit point2(const point2<T>& x):point2(x,x) {}

    template<typename U = T>
    U length() const {
        return static_cast<U>(dist(this->a,this->b));
    }

    /* 求点p到线段的距离 */
    template<typename U>
    T dis_point_segment(const point2<U>& p) {
        if (sign(dot(p - this->a,this->b - this->a)) < 0) return (p - this->a).norm();
        if (sign(dot(p - this->b,this->a - this->b)) < 0) return (p - this->b).norm();
        return std::abs(det(this->a - p,this->b - p) / this->length());
    }

    /* 求点p到线段的垂足 */
    template<typename U>
    point2<U> point_proj_line(const point2<U>& p) {

    }
};

using line2d = line2<double>;
}
