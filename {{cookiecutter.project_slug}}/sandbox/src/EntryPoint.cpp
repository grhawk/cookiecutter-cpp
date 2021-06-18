
#include <iostream>

#include "Sandbox.h"

int main(int argc, char* argv[])
{
    auto* sandbox = new Sandbox();
    std::cout << sandbox->message() << std::endl;
    delete sandbox;
}