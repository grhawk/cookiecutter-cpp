#!/usr/bin/env python
import os
import shutil
import subprocess
from contextlib import contextmanager

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_folder(folderpath):
    shutil.rmtree(folderpath)


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    #if '{{ cookiecutter.command_line_interface }}' == 'CLI11':
        #subprocess.call(('git', 'submodule', 'add', '-b', 'main', 'git@github.com:CLIUtils/CLI11.git', 'libs/CLI11'))

    if '{{ cookiecutter.logging_system }}' != 'y':
        remove_folder('logging')

    if '{{ cookiecutter.library_setup }}' == 'n':
        remove_folder('engine')


    subprocess.call(('git', 'init', '--initial-branch=main'))
    subprocess.call(('git', 'add', '.'))
    subprocess.call(('git', 'commit', '-m', 'Let there be light: and there was light.'))

