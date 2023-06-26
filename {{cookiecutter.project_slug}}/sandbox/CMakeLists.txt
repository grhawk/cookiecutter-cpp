set(PROJECT ${CPACK_PROJECT_NAME}-sandbox)

project(${PROJECT} VERSION {{cookiecutter.version}})

add_subdirectory(tests)

{% if cookiecutter.command_line_interface == 'CLI11' -%}find_package(CLI11){% endif %}

{% if cookiecutter.library_setup == 'y' -%}include_directories(${CMAKE_SOURCE_DIR}/engine/src) ${CPACK_PROJECT_NAME}-engine){% endif %}
add_executable(${PROJECT_NAME} src/EntryPoint.cpp src/Sandbox.cpp src/Sandbox.h)
add_library(${PROJECT_NAME}-lib EXCLUDE_FROM_ALL src/Sandbox.cpp src/Sandbox.h)


target_link_libraries(${PROJECT_NAME}
        {% if cookiecutter.library_setup == 'y' -%}${CPACK_PROJECT_NAME}-engine
        {% endif -%}
        {% if cookiecutter.command_line_interface == 'CLI11' -%}CLI11::CLI11
        {% endif -%}
        {% if cookiecutter.logging_system == 'y' -%}Logging{%- endif -%})
target_link_libraries(${PROJECT_NAME}-lib
        {% if cookiecutter.library_setup == 'y' -%}${CPACK_PROJECT_NAME}-engine
        {% endif -%}
        {% if cookiecutter.command_line_interface == 'CLI11' -%}CLI11::CLI11
        {% endif -%}
        {% if cookiecutter.logging_system == 'y' -%}Logging{%- endif -%})

