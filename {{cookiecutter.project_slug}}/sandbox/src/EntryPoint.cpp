
{%- if cookiecutter.command_line_interface == 'CLI11' -%}#include <CLI/CLI.hpp>
{% endif -%}
{% if cookiecutter.logging_system == 'y' -%}#include <Log.h>
{% endif -%}
#include <iostream>

#include "Sandbox.h"

int main(int argc, char* argv[])
{
    {%- if cookiecutter.logging_system == 'y' %}
    logging::Log LOGGER = logging::Log();
    LOG_ERROR("example of logger");
   {% endif %}
    {% if cookiecutter.command_line_interface == 'CLI11' %}std::string addToMessage = "CLI11 Console support activated!";

    CLI::App cli{"App description"};
    cli.add_option("Add to message",
                   addToMessage,
                   "String to append to message");
    CLI11_PARSE(cli, argc, argv);

    {% else -%}
    std::string addToMessage = "Console support has not been activated!";

    {% endif -%}
    auto* sandbox = new Sandbox();
    std::cout << sandbox->message() << std::endl;
    std::cout << addToMessage << std::endl;
    delete sandbox;
}
