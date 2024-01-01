
include_directories(${PROJECT_SOURCE_DIR}/src)
include_directories(${CMAKE_SOURCE_DIR}/engine/src)

find_package(Catch2 3 REQUIRED)

add_executable(${PROJECT_NAME}-test test1.cpp)
target_link_libraries(${PROJECT_NAME}-test PRIVATE Catch2::Catch2WithMain ${PROJECT_NAME}-lib)

include(CTest)
include(Catch)
catch_discover_tests(${PROJECT_NAME}-test)
