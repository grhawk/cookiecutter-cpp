cmake_minimum_required(VERSION 3.15.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
#set(CMAKE_CXX_EXTENSIONS OFF)

set(PROJECT {{cookiecutter.project_slug}})

project(${PROJECT} VERSION {{cookiecutter.version}})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "This variable is needed by conan.cmake." FORCE)
endif()

list(APPEND dependencies
        {% if cookiecutter.logging_system == 'y' -%}spdlog/1.11.0{% endif %}
        {% if cookiecutter.command_line_interface == 'CLI11' -%}cli11/2.3.2{% endif %}
        gtest/cci.20210126)

include(cmake/conan2.cmake)
include(cmake/gtest.cmake)

{% if cookiecutter.library_setup == 'y' -%}add_subdirectory(engine){% endif %}
add_subdirectory(sandbox)

{% if cookiecutter.logging_system == 'y' -%}
add_subdirectory(logging EXCLUDE_FROM_ALL)
{% endif %}
