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

{% if cookiecutter.unit_testing_framework == 'GoogleTest' -%} include(cmake/gtest.cmake) {% endif %}

{% if cookiecutter.library_setup == 'y' -%}add_subdirectory(engine){% endif %}
add_subdirectory(sandbox)

{% if cookiecutter.logging_system == 'y' -%}
add_subdirectory(logging EXCLUDE_FROM_ALL)
{% endif %}
