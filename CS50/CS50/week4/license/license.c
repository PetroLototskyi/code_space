#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7 && idx <8)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        /* plates[idx] = buffer;*/

        // Allocate memory for plate number and copy
        plates[idx] = malloc(7); // Allocate memory for each plate number
        strcpy(plates[idx], buffer); // Copy plate number
        //
        //


        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);

        //
        free(plates[i]); // Free allocated memory for each plate
        //

    }
    //
     // Close file
    fclose(infile);

    return 0;
    //

}
