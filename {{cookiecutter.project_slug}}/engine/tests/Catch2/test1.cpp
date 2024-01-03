#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"

#include<catch2/catch_test_macros.hpp>

#include<{{cookiecutter.project_slug}}.h>

TEST_CASE("dummyFunction() returns always `Hello!`", "[dummyFunction]"){
    std::string expected = "Hello!";
    REQUIRE({{cookiecutter.project_slug}}::Application::dummyFunction() == expected);
}

#pragma clang diagnostic pop
