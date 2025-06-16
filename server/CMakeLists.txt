cmake_minimum_required(VERSION 3.10)
project(GameServer C)

# Include directories
include_directories(include)

# Source files
set(SERVER_SOURCES
    src/main.c
    src/game.c
    src/network.c
)

# Add executable
add_executable(GameServer ${SERVER_SOURCES})

# Add test executable
add_executable(run_tests tests/test_game.c tests/test_network.c) # Assuming Unity/CUnit tests are self-contained or linked

# Add tests
add_test(NAME GameServerUnitTests COMMAND run_tests)
