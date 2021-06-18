#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err58-cpp"
#include<gtest/gtest.h>

#include<Sandbox.h>

TEST(Example, ExampleTest){
Sandbox sandbox = Sandbox();
ASSERT_STREQ(sandbox.message(), "Hello!");
}

#pragma clang diagnostic pop
