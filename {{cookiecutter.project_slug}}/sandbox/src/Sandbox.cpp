//
// Created by Petraglia Riccardo, INI-CLD-TCL on 24.05.21.
//

#include <Haribo.h>

class Sandbox : public Haribo::Application
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