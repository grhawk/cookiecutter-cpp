#include <iostream>

#include "application.h"

namespace {{cookiecutter.project_slug}} {

  Application::Application() 
  {
    std::cout << "Starting application!" << std::endl;
  }

  const char* Application::dummyFunction()
  {
    return "Hello!";
  }

  Application::~Application() = default;
}
