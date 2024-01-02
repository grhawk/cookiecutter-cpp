#!/usr/bin/env python
import os
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path

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

    test_folders = [
        Path('engine/tests'),
        Path('sandbox/tests')
    ]
    for test_folder in test_folders:
        for folder in test_folder.iterdir():
            if '{{ cookiecutter.unit_testing_framework }}' == folder.name:
                for file in folder.iterdir():
                    shutil.move(file, folder.parent)
            shutil.rmtree(folder)

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

    if '{{ cookiecutter.unit_testing_framework }}' != 'GoogleTest':
        remove_file('cmake/gtest.cmake')


    subprocess.call(('git', 'init', '--initial-branch=main'))
    subprocess.call(('git', 'add', '.'))
    subprocess.call(('git', 'commit', '-m', 'Let there be light: and there was light.'))

