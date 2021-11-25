#include <stdio.h>
#include <unistd.h>

int main()
{
    if (fork() == 0)
    {
        printf("Child");
        execlp("/bin/ls", "ls", "-al", NULL);
    }
    else
    {
        printf("Parent");
    }

}