
set(PROJECT ${CPACK_PROJECT_NAME}-engine)

project(${PROJECT} VERSION 0.1.0)

add_subdirectory(tests)

add_library(${PROJECT_NAME} src/{{cookiecutter.project_slug}}.h src/{{cookiecutter.project_slug}}/core.h src/{{cookiecutter.project_slug}}/Application.cpp src/{{cookiecutter.project_slug}}/Application.h)

