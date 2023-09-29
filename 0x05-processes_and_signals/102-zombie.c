#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - loops to infinity
 * Return: 0
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
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pidme;

	i = 0;
	while (i < 5)
	{
		pidme = fork();
		if (pidme)
			printf("Zombie process created, PID: %i\n", pidme);
		else
		{
			exit(0);
		}
		i++;
	}
	infinite_while;
	return (0);
}
