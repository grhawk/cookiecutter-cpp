//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#ifndef {{cookiecutter.project_uppercase}}_APPLICATION_H
#define {{cookiecutter.project_uppercase}}_APPLICATION_H

#include "Core.h"

namespace Haribo {
    class HR_API Application {
    public:
        Application();
        virtual ~Application();

        void run();
    };
}


#endif //{{cookiecutter.project_uppercase}}_APPLICATION_H
