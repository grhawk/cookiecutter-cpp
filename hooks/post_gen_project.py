#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.command_line_interface }}' == 'CLI11':
        import subprocess
        subprocess.call(('git', 'init'))
        subprocess.call(('git', 'submodule', 'add', 'git@github.com:CLIUtils/CLI11.git', 'libs/CLI11'))

    if '{{ cookiecutter.logging_system }}' == 'y':
        import subprocess
        subprocess.call(('git', 'init'))
        subprocess.call(('git', 'submodule', 'add', 'git@github.com:gabime/spdlog.git', 'libs/spdlog'))