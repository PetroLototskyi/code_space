#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // if more then one input exit
    if (argc != 2)
    {
        return 1;
    }
    // Image opening
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        return 1;
    }

    uint8_t *buffer = malloc(BLOCK_SIZE);
    if (buffer == NULL)
    {
        fclose(file);
        return 1;
    }

    int jpgCount = 0;
    FILE *jpegFile = NULL;

    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG file (if any)
            if (jpegFile != NULL)
            {
                fclose(jpegFile);
            }

            // Create new JPEG
            char filename[8];
            sprintf(filename, "%03i.jpg", jpgCount++);
            jpegFile = fopen(filename, "w");
            if (jpegFile == NULL)
            {
                free(buffer);
                fclose(file);
                return 1;
            }

            // Put buffer to JPEG file
            fwrite(buffer, 1, BLOCK_SIZE, jpegFile);
        }
        else if (jpegFile != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, jpegFile);
        }
    }

    if (jpegFile != NULL)
    {
        fclose(jpegFile);
    }

    fclose(file);

    free(buffer);

    return 0;
}
