
{% if cookiecutter.command_line_interface == 'CLI11' -%}#include <CLI/CLI.hpp>{% endif %}
#include <iostream>

#include "Sandbox.h"

int main(int argc, char* argv[])
{
    std::string addToMessage = "CLI11 is not activated!";
    {% if cookiecutter.command_line_interface == 'CLI11' -%}CLI::App cli{"App description"};
    cli.add_option("Add to message",
                   addToMessage,
                   "String to append to message");
    CLI11_PARSE(cli, argc, argv);{% endif %}

    auto* sandbox = new Sandbox();
    std::cout << sandbox->message() << std::endl;
    std::cout << addToMessage << std::endl;
    delete sandbox;
}