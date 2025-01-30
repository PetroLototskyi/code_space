#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt for height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1  || height > 8);

    //Declere variables
    int i, j, k;

    //Creating main loop for rows
    for (i = 1; i <= height; i++)
    {
        //Loop for white spaces
        for (j = i; j <= height - 1; j++)
        {
            printf(" ");
        }

        //Loop for "#"
        for (k = j - 1; k >= height - i; k--)
        {
            printf("#");
        }

        //Print two spases after "#"
        printf("  ");

        //Print same amount of "#"  as before two white spaces
        for (k = j - 1; k >= height - i; k--)
        {
            printf("#");
        }
        //Jump to new raw
        printf("\n");
    }
}
