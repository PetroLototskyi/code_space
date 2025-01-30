// Prints an integer
// #include <cs50.h>
#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%p\n", s);
    printf("%s\n", s);
    printf("%s\n", s+1);
    printf("%s\n", s+2);
    printf("%c\n", s[3]);
}