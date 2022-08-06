#ifndef CREATIONAL_SINGLETON_H
#define CREATIONAL_SINGLETON_H
#include <string>

namespace DesignPatterns
{
namespace Creational
{
class Singleton
{
public:
    //! A static method that check and return only one instance.
    //! @param[in] value
    //! @return a single instance of the class
    static Singleton& instance(const std::string& value);

    //! Singleton instance should not be cloneable.
    Singleton(const Singleton&) = delete;
    //! Singleton instance should not be ssignable.
    void operator=(const Singleton&) = delete;

    //! brief demo method to  get the instance value.
    //! return value
    std::string get_value();

private:
    //!
    std::string value_;
    //! Constructor.
    explicit Singleton(const std::string& value);
    //! Destructor.
    ~Singleton() = default;

};
}
}
#endif // !CREATIONAL_SINGLETON_H
