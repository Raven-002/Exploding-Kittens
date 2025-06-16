cmake_minimum_required(VERSION 3.25)
project(GameServer C)

# Include directories
add_subdirectory(src/game)
add_subdirectory(src/network)

# Source files
set(SERVER_SOURCES
    src/main.c
)

# Add executable
add_executable(GameServer ${SERVER_SOURCES})
target_link_libraries(GameServer game network)
set_property(TARGET GameServer PROPERTY C_STANDARD 99)
set_property(TARGET GameServer PROPERTY C_STANDARD_REQUIRED YES)

# Add test executable
add_executable(run_tests tests/test_game.c tests/test_network.c) # Assuming Unity/CUnit tests are self-contained or linked
target_link_libraries(run_tests game network)
set_property(TARGET run_tests PROPERTY C_STANDARD 99)
set_property(TARGET run_tests PROPERTY C_STANDARD_REQUIRED YES)

# Add tests
add_test(NAME GameServerUnitTests COMMAND run_tests)
