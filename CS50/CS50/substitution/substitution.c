#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool valid(string key);

int main(int argc, string argv[])
{
    // check if there are 2 arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // check if there are 26 character in the key
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // check if all characters alphabethic
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must contain only alphabetic characters.\n");
            return 1;
        }
    }
    if (!valid(argv[1]))
    {
        printf("All 26 key characters must be unique.\n");
        return 1;
    }

    string input = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(input); i++)
    {

        if (isalpha(input[i]))
        {
            char replacement;

            if (islower(input[i]))
            {
                replacement = tolower(argv[1][input[i] - 'a']);
            }
            else
            {
                replacement = toupper(argv[1][input[i] - 'A']);
            }
            printf("%c", replacement);
        }
        else
        {
            printf("%c", input[i]);
        }
    }

    printf("\n");
}
// validete if key contains only unique characters
bool valid(string key)
{
    for (int i = 0; i < 26; i++)
    {
        key[i] = toupper(key[i]);
    }

    for (int i = 0; i < 26; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                printf("There are dublicate in key %c\n", key[i]);
                return false;
            }
        }
    }
    return true;
}