//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#include "application.h"
#include <iostream>

namespace {{cookiecutter.project_slug}} {

  Application::Application() 
  {
    std::cout << "Starting application!" << std::endl;
  }

  int application::dummyFunction()
  {
    return 0;
  }

  Application::~Application() = default;
}
