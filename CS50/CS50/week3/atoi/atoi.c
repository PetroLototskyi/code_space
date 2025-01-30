#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // Base case: if the input string is empty, return 0
    if (input[0] == '\0')
    {
        return 0;
    }

    // Get the last character of the string and convert it to an integer
    int digit = input[strlen(input) - 1] - '0';

    // Remove the last character from the string
    input[strlen(input) - 1] = '\0';

    // Make a recursive call to process the shortened string
    int remaining = convert(input);

    // Multiply the value obtained from the recursive call by 10 and add the current digit
    return remaining * 10 + digit;
}