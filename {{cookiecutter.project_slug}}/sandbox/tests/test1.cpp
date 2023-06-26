#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"
#include<gtest/gtest.h>

{% if cookiecutter.logging_system == 'y' -%}#include <Log.h>{% endif %}
#include<Sandbox.h>

{% if cookiecutter.logging_system == 'y' -%}logging::Log LOGGER = logging::Log();
{% endif %}
TEST(Example, ExampleTest){
  Sandbox sandbox = Sandbox();
  {% if cookiecutter.logging_system == 'y' -%}LOG_INFO("Testing");{% endif %}
  {% if cookiecutter.library_setup == 'y' -%}
      const char* expected_message = "Hello!";
  {% else %}
      const char* expected_message = "Simple starter created!";
  {% endif %}
  ASSERT_STREQ(sandbox.message(), expected_message);
}

#pragma clang diagnostic pop
