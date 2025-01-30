#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Lets assign new color
    RGBTRIPLE updatedColor = {0x96, 0xFA, 0x14};


    // itereate though pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Change black pixels to updated color
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00)
            {
                image[i][j] = updatedColor;
            }
        }
    }
}
