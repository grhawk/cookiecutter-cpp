
set(PROJECT ${CPACK_PROJECT_NAME}-engine)

project(${PROJECT} VERSION 0.1.0)

add_subdirectory(tests)

add_library(${PROJECT_NAME} src/{{cookiecutter.project_slug}}.h src/{{cookiecutter.project_slug}}/core.h src/{{cookiecutter.project_slug}}/application.cpp src/{{cookiecutter.project_slug}}/application.h)
{% if cookiecutter.logging_system == 'y' -%}target_link_libraries(${PROJECT_NAME} PUBLIC Logging) {% endif %}