#ifndef {{cookiecutter.project_uppercase}}_SANDBOX_H
#define {{cookiecutter.project_uppercase}}_SANDBOX_H

#include <{{cookiecutter.project_slug}}.h>

class Sandbox
{
private:
    const char* p_message =
            {{cookiecutter.project_slug}}::Application::dummyFunction();
public:
    Sandbox() = default;
    ~Sandbox() = default;
    const char* message();
};


#endif //{{cookiecutter.project_uppercase}}_SANDBOX_H
