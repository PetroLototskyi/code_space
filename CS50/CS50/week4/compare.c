// Compares two integers

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
      // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");
    int count = 0;

    // Compare strings
    if (strlen(s)!=strlen(t))
    {
        count ++;
        printf("Different\n");
    }
    else if (strlen(s)==strlen(t))
    {
        for (int i =0; i < strlen(s); i++)
        {
            if (strcmp(s+i,t+i)!= 0)
        {
            count++;
        printf("Different\n");
        break;
        }
        }

    }
    if (count == 0)
    {
        printf("Same\n");
    }
}