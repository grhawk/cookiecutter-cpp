//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#include "Application.h"
#include <iostream>

namespace {{cookiecutter.project_slug}} {

    Application::Application() = default;

    Application::~Application() = default;

    _Noreturn void Application::run() {
        while(true){
            std::cout << "Running the default application!" << std::endl;
        };
    }
}