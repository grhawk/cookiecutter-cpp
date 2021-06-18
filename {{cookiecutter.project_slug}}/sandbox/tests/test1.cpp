#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"
#include<gtest/gtest.h>

{% if cookiecutter.logging_system == 'y' -%}#include <Log.h>{% endif %}
#include<Sandbox.h>

{% if cookiecutter.logging_system == 'y' -%}logging::Log LOGGER = logging::Log();
{% endif %}
TEST(Example, ExampleTest){
Sandbox sandbox = Sandbox();
ASSERT_STREQ(sandbox.message(), "Hello!");
}

#pragma clang diagnostic pop
