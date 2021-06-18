//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#ifndef {{cookiecutter.project_uppercase}}_APPLICATION_H
#define {{cookiecutter.project_uppercase}}_APPLICATION_H

#include "core.h"

namespace {{cookiecutter.project_slug}} {
  class HR_API Application {
  public:
      Application();
      ~Application();
      static int dummyFunction();
  };
}


#endif //{{cookiecutter.project_uppercase}}_APPLICATION_H
