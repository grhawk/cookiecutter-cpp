cmake_minimum_required(VERSION 3.10.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
#set(CMAKE_CXX_EXTENSIONS OFF)

set(PROJECT {{cookiecutter.project_slug}})

project(${PROJECT} VERSION {{cookiecutter.version}})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

include(cmake/gtest.cmake)

add_subdirectory(engine)
add_subdirectory(sandbox)
{% if cookiecutter.command_line_interface == 'CLI11' -%}
add_subdirectory(libs/CLI11 EXCLUDE_FROM_ALL)
{% endif %}
{% if cookiecutter.logging_system == 'y' -%}
add_subdirectory(libs/spdlog EXCLUDE_FROM_ALL)
add_subdirectory(logging EXCLUDE_FROM_ALL)
{% endif %}
