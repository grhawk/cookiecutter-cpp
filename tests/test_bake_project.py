import datetime
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager

from cookiecutter.utils import rmtree


def pytest_exception_interact(node, call, report):
    if report.failed:
        input("Press any key to delete the test folder...")
        print("Use `-s` to stop the test here!")
        raise call.excinfo


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


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = result.project_path
    project_slug = project_path.stem
    project_dir = project_path / project_slug
    return project_path, project_slug, project_dir


def build_and_test(result):
    build_dir = result.project_path / "build"
    #run_inside_dir("cat ./sandbox/src/EntryPoint.cpp", str(result.project))
    assert run_inside_dir('mkdir build', str(result.project_path)) == 0
    assert run_inside_dir('cmake -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=cmake/conan_provider.cmake ..', build_dir) == 0
    assert run_inside_dir('cmake --build .', build_dir) == 0
    assert run_inside_dir('./sandbox/tests/cpp_boilerplate-sandbox-test', build_dir) == 0
    assert run_inside_dir('./sandbox/cpp_boilerplate-sandbox', build_dir) == 0
    out = check_output_inside_dir('./sandbox/cpp_boilerplate-sandbox', build_dir)
    print(b'#' + out + b'#')
    return out


def assert_simple_starter_setup(output):
    assert (b"Simple starter created!" in output)


def assert_library_setup(output, result):
    assert run_inside_dir('./engine/tests/cpp_boilerplate-engine-test', str(result.project_path / "build")) == 0
    assert (b"Simple starter created!" not in output)


def assert_logger_enabled(output, bake_result=None):
    assert run_inside_dir('grep -q -i -r spdlog', str(bake_result.project_path)) == 0
    assert run_inside_dir('grep -q -i -r LOGGER', str(bake_result.project_path)) == 0
    assert (b"(error) example of logger" in output)


def assert_logger_not_enabled(output, bake_result=None):
    assert run_inside_dir('grep -q -v -i -r spdlog', str(bake_result.project_path)) == 0
    assert run_inside_dir('grep -q -v -i -r LOGGER', str(bake_result.project_path)) == 0
    assert (b"(error) example of logger" not in output)


def assert_cli_enabled(output, bake_result=None):
    assert run_inside_dir('grep -q -i -r CLI11', str(bake_result.project_path)) == 0
    assert (b"CLI11 Console support activated!" in output)


def assert_cli_not_enabled(output, bake_result):
    assert run_inside_dir('grep -v -q -i -r CLI11', str(bake_result.project_path)) == 0
    assert (b"Console support has not been activated!" in output)

def assert_gtest_enabled_library_setup(output, bake_result):
    main_output = check_output_inside_dir('grep -i -r GTest::gtest_main', str(bake_result.project_path))
    assert b"sandbox/tests/CMakeLists.txt" in main_output
    assert b"engine/tests/CMakeLists.txt" in main_output
    discover_tests_output = check_output_inside_dir('grep -i -r  gtest_discover_tests', str(bake_result.project_path))
    assert b"sandbox/tests/CMakeLists.txt" in discover_tests_output
    assert b"engine/tests/CMakeLists.txt" in discover_tests_output
    include_output = check_output_inside_dir('grep -i -r #include<gtest/gtest.h>', str(bake_result.project_path))
    assert b"sandbox/tests/test1.cpp" in include_output
    assert b"engine/tests/test1.cpp" in include_output
    assert run_inside_dir('grep -i -r gtest/', str(bake_result.project_path)) == 0
    assert (b"GoogleTest unit testing framework activated!" in output)

def assert_catch2_enabled_library_setup(output, bake_result):
    main_output = check_output_inside_dir('grep -i -r Catch2::Catch2WithMain', str(bake_result.project_path))
    assert b"sandbox/tests/CMakeLists.txt" in main_output
    assert b"engine/tests/CMakeLists.txt" in main_output
    discover_tests_output = check_output_inside_dir('grep -i -r  catch_discover_tests', str(bake_result.project_path))
    assert b"sandbox/tests/CMakeLists.txt" in discover_tests_output
    assert b"engine/tests/CMakeLists.txt" in discover_tests_output
    include_output = check_output_inside_dir('grep -i -r <catch2/catch_test_macros.hpp>', str(bake_result.project_path))
    assert b"sandbox/tests/test1.cpp" in include_output
    assert b"engine/tests/test1.cpp" in include_output
    assert run_inside_dir('grep -i -r catch2/3.', str(bake_result.project_path)) == 0
    assert (b"Catch2 unit testing framework activated!" in output)

def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path / 'LICENSE'
        now = datetime.datetime.now()
        with license_file_path.open() as fp:
            assert str(now.year) in fp.read()


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert 'CMakeLists.txt' in found_toplevel_files
        assert '.gitignore' in found_toplevel_files
        assert 'README.rst' in  found_toplevel_files


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        print("test_bake_and_run_tests path", str(result.project_path))
        assert_simple_starter_setup(output)
        assert_logger_enabled(output, result)
        assert_cli_enabled(output, result)


def test_bake_withspecialchars_and_run_tests(cookies):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    with bake_in_temp_dir(
        cookies,
        extra_context={'full_name': 'name "quote" name'}
    ) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        assert_simple_starter_setup(output)
        assert_logger_enabled(output, result)
        assert_cli_enabled(output, result)



def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir(
        cookies,
        extra_context={'full_name': "O'connor"}
    ) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        assert_simple_starter_setup(output)
        assert_logger_enabled(output, result)
        assert_cli_enabled(output, result)

def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'create_author_file': 'n'}
    ) as result:
        found_toplevel_files = get_top_level_files(result)
        assert 'AUTHORS.rst' not in found_toplevel_files
        # doc_files = [f.basename for f in result.project_path.join('docs').listdir()]
        # assert 'authors.rst' not in doc_files

        # Assert there are no spaces in the toc tree
        # docs_index_path = result.project_path.join('docs/index.rst')
        # with open(str(docs_index_path)) as index_file:
        #     assert 'contributing\n   history' in index_file.read()

        # Check that
        manifest_path = result.project_path / 'MANIFEST.in'
        with open(str(manifest_path)) as manifest_file:
            assert 'AUTHORS.rst' not in manifest_file.read()


def get_top_level_files(result):
    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    return found_toplevel_files


def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        # The supplied Makefile does not support win32
        if sys.platform != "win32":
            build_and_test(result)
            output = check_output_inside_dir(
                'make help',
                str(result.project_path / "build")
            )
            assert b"cpp_boilerplate-sandbox" in \
                output


def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT license': 'MIT ',
        'BSD license': 'Redistributions of source code must retain the ' +
                       'above copyright notice, this',
        'ISC license': 'ISC License',
        'Apache Software License 2.0':
            'Licensed under the Apache License, Version 2.0',
        'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies,
            extra_context={'open_source_license': license}
        ) as result:
            assert target_string in (result.project_path / 'LICENSE').open().read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'open_source_license': 'Not open source'}
    ) as result:

        found_toplevel_files = get_top_level_files(result)
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in (result.project_path / 'README.rst').open().read()


def test_bake_with_no_console_script(cookies):
    context = {'command_line_interface': "No command-line interface"}
    result = cookies.bake(extra_context=context)
    output = build_and_test(result)
    assert_simple_starter_setup(output)
    assert_logger_enabled(output, result)
    assert_cli_not_enabled(output, result)



def test_bake_with_no_logging_system(cookies):
    context = {'logging_system': 'n'}
    result = cookies.bake(extra_context=context)
    output = build_and_test(result)
    assert_simple_starter_setup(output)
    assert_logger_not_enabled(output, result)
    assert_cli_enabled(output, result)


def test_bake_with_no_logging_system_and_no_cli(cookies):
    context = {'logging_system': 'n',
               'command_line_interface': "No command-line interface"}
    result = cookies.bake(extra_context=context)
    output = build_and_test(result)
    assert_simple_starter_setup(output)
    assert_logger_not_enabled(output, result)
    assert_cli_not_enabled(output, result)

def test_bake_library_setup_and_run_tests(cookies):
    context = {'library_setup': 'y'}
    with bake_in_temp_dir(cookies,
                          extra_context=context) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        assert_library_setup(output, result)
        assert_logger_enabled(output, result)
        assert_cli_enabled(output, result)


def test_bake_library_setup_with_no_logging_system(cookies):
    context = {'logging_system': 'n',
               'library_setup': 'y'}
    result = cookies.bake(extra_context=context)
    output = build_and_test(result)
    assert_library_setup(output, result)
    assert_logger_not_enabled(output, result)
    assert_cli_enabled(output, result)

def test_bake_library_setup_with_no_logging_system_and_no_cli(cookies):
    context = {'logging_system': 'n',
               'command_line_interface': "No command-line interface",
               'library_setup': 'y'}
    result = cookies.bake(extra_context=context)
    output = build_and_test(result)
    assert_library_setup(output, result)
    assert_cli_not_enabled(output, result)
    assert_logger_not_enabled(output, result)


def test_bake_library_setup_with_gtest(cookies):
    context = {'unit_testing_framework': 'GoogleTest',
               'library_setup': 'y'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        assert_library_setup(output, result)
        assert_gtest_enabled_library_setup(output, result)

def test_bake_library_setup_with_catch2(cookies):
    context = {'unit_testing_framework': 'Catch2',
               'library_setup': 'y'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        output = build_and_test(result)
        assert_library_setup(output, result)
        assert_catch2_enabled_library_setup(output, result)
