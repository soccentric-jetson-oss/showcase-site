#include <catch2/catch_test_macros.hpp>
#include <thread>
#include <chrono>
#include <atomic>

TEST_CASE("Integration test 1", "[integration]") {
    std::atomic<int> counter{0};
    std::thread t([&]() { counter = 42; });
    t.join();
    REQUIRE(counter == 42);
}

TEST_CASE("Integration test 2", "[integration]") {
    auto start = std::chrono::steady_clock::now();
    std::this_thread::sleep_for(std::chrono::milliseconds(5));
    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    REQUIRE(elapsed >= 4);
}
