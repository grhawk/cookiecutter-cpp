#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"
#include<catch2/catch_test_macros.hpp>

{% if cookiecutter.logging_system == 'y' -%}#include <Log.h>{% endif %}
#include<Sandbox.h>

{% if cookiecutter.logging_system == 'y' -%}logging::Log LOGGER = logging::Log();
{% endif %}
TEST_CASE("sandbox.message() should always be `Hello!`", "[sandbox]"){
  Sandbox sandbox = Sandbox();
  {% if cookiecutter.logging_system == 'y' -%}LOG_INFO("Testing");{% endif %}
  {% if cookiecutter.library_setup == 'y' -%}
      const char* expected_message = "Hello!";
  {% else %}
      const char* expected_message = "Simple starter created!";
  {% endif %}
  REQUIRE(sandbox.message() == expected_message);
}

#pragma clang diagnostic pop
