#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

float count_letters(string text);
int count_words(string text);
float count_sentences(string text);

int main(void)
{

    string text = get_string("Text: ");
    int index = round(0.0588 * count_letters(text) - 0.296 * count_sentences(text) - 15.8);
    if (index < 1)
        printf("Before Grade 1\n");
    else if (index >= 16)
        printf("Grade 16+\n");
    else
        printf("Grade %i\n", index);
}

float count_letters(string text)
{
    float result = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
            result++;
    }
    // printf("Number of letters is %f\n", result);
    return result / count_words(text) * 100;
}

int count_words(string text)
{
    int result = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
            result++;
    }
    // printf("Number of worlds is %i\n", result+1);
    return result + 1;
}

float count_sentences(string text)
{
    float result = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            result++;
    }
    // printf("Number of sentences is %f\n", result);
    return result / count_words(text) * 100;
}
