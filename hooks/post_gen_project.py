#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    
    
    subprocess.call(('git', 'init'))
    subprocess.call(('git', 'add', '.'))
    
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.command_line_interface }}' == 'CLI11':
        subprocess.call(('git', 'submodule', 'add', 'git@github.com:CLIUtils/CLI11.git', 'libs/CLI11'))

    if '{{ cookiecutter.logging_system }}' == 'y':
        subprocess.call(('git', 'submodule', 'add', 'git@github.com:gabime/spdlog.git', 'libs/spdlog'))


    subprocess.call(('git', 'commit', '-m', 'Initial commit'))

