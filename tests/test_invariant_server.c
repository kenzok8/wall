#include <check.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

START_TEST(test_memory_leak_obfs_compatible)
{
    // Invariant: Memory allocated during obfs_compatible processing must be freed regardless of decode outcome
    const char *payloads[] = {
        "\x00\x00\x00\x00\x00\x00\x00\x00",  // Zero-length boundary case
        "\x01\x02\x03\x04\x05\x06\x07\x08",  // Valid normal input
        "A" * 1024,                          // Large payload
        "\xff\xff\xff\xff\xff\xff\xff\xff",  // Max boundary values
        ""                                   // Empty string
    };
    int num_payloads = sizeof(payloads) / sizeof(payloads[0]);

    for (int i = 0; i < num_payloads; i++) {
        pid_t pid = fork();
        if (pid == 0) {
            // Child process: run actual server with payload
            execl("./test_server", "test_server", payloads[i], NULL);
            exit(EXIT_FAILURE);  // execl failed
        } else if (pid > 0) {
            int status;
            waitpid(pid, &status, 0);
            
            // Check for abnormal termination indicating memory issues
            ck_assert_msg(WIFEXITED(status) && WEXITSTATUS(status) == 0,
                         "Server crashed or leaked memory with payload %d", i);
        }
    }
}
END_TEST

Suite *security_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Security");
    tc_core = tcase_create("Core");

    tcase_add_test(tc_core, test_memory_leak_obfs_compatible);
    suite_add_tcase(s, tc_core);

    return s;
}

int main(void)
{
    int number_failed;
    Suite *s;
    SRunner *sr;

    s = security_suite();
    sr = srunner_create(s);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);

    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}