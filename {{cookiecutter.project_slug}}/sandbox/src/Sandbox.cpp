//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#include <{{cookiecutter.project_slug}}.h>

class Sandbox : public {{cookiecutter.project_slug}}::Application
{
public:
    Sandbox()= default;
    ~Sandbox() override = default;
};

int main()
{
    Sandbox* sandbox = new Sandbox();
    sandbox->run();
    delete sandbox;
}