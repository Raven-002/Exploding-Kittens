enable_testing()

# Add tests for each module
foreach(module ${GAME_SERVER_MODULES})
    string(TOUPPER ${module} MODULE_UPPER)
    add_executable(test_${module} ${GAME_SERVER_TESTS_DIR}/test_${module}.c)
    target_link_libraries(test_${module} ${module})
    add_test(NAME test_${module} COMMAND test_${module})
endforeach()
