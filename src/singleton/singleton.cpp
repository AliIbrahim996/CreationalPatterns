#include "singleton/singleton.h"

#include <iostream>

namespace DesignPatterns
{
namespace Creational
{
Singleton::Singleton(const std::string& value)
{
    std::cout << "New instance initialized!" << std::endl;
    this->value_ = value;
}

Singleton& Singleton::instance(const std::string& value)
{
    static Singleton instance(value);
    return instance;
}

std::string Singleton::get_value()
{
    return this->value_;
}
}
} // namespace DesignPatterns

