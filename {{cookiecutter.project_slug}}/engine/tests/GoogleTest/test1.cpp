#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"

#include<gtest/gtest.h>

#include<{{cookiecutter.project_slug}}.h>

TEST(Example, ExampleTest){
ASSERT_STREQ({{cookiecutter.project_slug}}::Application::dummyFunction(), "Hello!");
}

#pragma clang diagnostic pop