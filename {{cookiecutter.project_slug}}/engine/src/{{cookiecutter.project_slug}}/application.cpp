#include <iostream>
{% if cookiecutter.logging_system == 'y' -%}#include <Log.h>{% endif %}

#include "application.h"

namespace {{cookiecutter.project_slug}} {

  Application::Application() 
  {
    {% if cookiecutter.logging_system == 'y' -%}_LOG_CRITICAL("Logging is included!");{% endif %}
    std::cout << "Starting application!" << std::endl;
  }

  const char* Application::dummyFunction()
  {
    return "Hello!";
  }

  Application::~Application() = default;
}
