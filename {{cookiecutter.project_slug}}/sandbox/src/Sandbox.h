#ifndef {{cookiecutter.project_uppercase}}_SANDBOX_H
#define {{cookiecutter.project_uppercase}}_SANDBOX_H

{% if cookiecutter.library_setup == 'y' -%}#include <{{cookiecutter.project_slug}}.h>{% endif %}

class Sandbox
{
private:
{% if cookiecutter.library_setup == 'y' -%}
    const char* p_message =
            {{cookiecutter.project_slug}}::Application::dummyFunction();
    {{cookiecutter.project_slug}}::Application app;
{% else %}
    const char* p_message = "Simple starter created!";
{% endif %}
public:
{% if cookiecutter.library_setup == 'y' -%}
    Sandbox()
            : app({{cookiecutter.project_slug}}::Application()) {}
{% else %}
    Sandbox() = default;
{% endif %}
    ~Sandbox() = default;
    const char* message();
};


#endif //{{cookiecutter.project_uppercase}}_SANDBOX_H
