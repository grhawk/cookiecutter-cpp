CHANGELOG
=========

All the edit to the code should be described under the "Unreleased" tag as a
bullet list. The ci/cd automation will take care of moving them under the right
version tag at releasing time.

Versioning
----------
**[Unreleased]**
* Create a simpler stub by default.

**[3.0.3]**
* According to https://en.cppreference.com/w/cpp/language/identifiers, identifiers in "_[A-Z].*" are reserved to the implementation.
* Generated code has newlines as expected.
* More modern version of `cmake` do not have `-v` option.

**[3.0.2]**
* Improved documentation and added README to pkg-info.

**[3.0.1]**
* [FIX] Publishing should work now.

**[3.0.0]**
* Using CMAKE and CONAN2 to manage dependencies instead of submodules.
* [FIX] CircleCi pipeline. Tests run successfully.

**[2.0.2]**

**[2.0.1]**
* Improved documentation.
* spdlog version fixed to v1.8.5.

**[2.0.0]**
* Added a script to automate CHANGELOG management.
* [FIX] CircleCi version and publish.

**[0.2.0]**
* First release of Cookiecutter-C++ based on the `cookiecutter-pypackage`

**[0.1.0]**
* Not released.


