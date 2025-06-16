cmake_minimum_required(VERSION 3.25)
project(GameServer C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(GAME_SERVER_PROJECT_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
set(GAME_SERVER_SOURCE_DIR "${GAME_SERVER_PROJECT_DIR}/src")
set(GAME_SERVER_TESTS_DIR "${GAME_SERVER_PROJECT_DIR}/tests")

set(GAME_SERVER_MODULES
    game
    network
)

foreach(module ${GAME_SERVER_MODULES})
    add_subdirectory(${GAME_SERVER_SOURCE_DIR}/${module})
endforeach()

set(GAME_SERVER_SOURCES
    src/main.c
)

add_executable(GameServer ${GAME_SERVER_SOURCES})
target_link_libraries(GameServer game network)


include(tests/tests.cmake)
