#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Runs an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid > 0)
        {
            printf("Zombie process created, PID: %d\n", pid);
        }
        else if (pid == 0)
        {
            // Child process: immediately exit to become zombie
            exit(0);
        }
        else
        {
            perror("fork");
            return (1);
        }
    }

    // Parent process: run infinite loop
    infinite_while();

    return (0);
}