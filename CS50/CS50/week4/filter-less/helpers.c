#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    // loop throuh each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate averege from 3 color
            int average = (float) round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);

            // assign each color to averege
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop throuh each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // apply formula
            int sRed = (int) round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sGreen = (int) round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sBlue = (int) round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            // make 255 max if exided
            if (sRed > 255)
                sRed = 255;
            if (sGreen > 255)
                sGreen = 255;
            if (sBlue > 255)
                sBlue = 255;

            // change colors to calculated values
            image[i][j].rgbtRed = (BYTE) sRed;
            image[i][j].rgbtGreen = (BYTE) sGreen;
            image[i][j].rgbtBlue = (BYTE) sBlue;
        }
    }
}
// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop throuh each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++) // here we stop in midle of
                                            // the row. Becouse if we swap we do not need cross midle point
        {
            // Swaping using temporary value
            int jOposit = width - 1 - j;
            RGBTRIPLE t = image[i][j];
            image[i][j] = image[i][jOposit];
            image[i][jOposit] = t;
        }
    }
}
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy
    RGBTRIPLE duplicate[height][width];

    // Looping though each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = 0, green = 0, blue = 0;
            int count = 0;

            // check 3X3 square
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // location of pixel around
                    int ki = i + k;
                    int lj = j + l;

                    // bondary inspection
                    if (ki >= 0 && ki < height && lj >= 0 && lj < width)
                    {
                        // get sum of pixel numbers
                        red = red + image[ki][lj].rgbtRed;
                        green = green + image[ki][lj].rgbtGreen;
                        blue = blue + image[ki][lj].rgbtBlue;
                        count++;
                    }
                }
            }

            // put averege value in dublicate
            duplicate[i][j].rgbtRed = (BYTE) round((float) red / count);
            duplicate[i][j].rgbtGreen = (BYTE) round((float) green / count);
            duplicate[i][j].rgbtBlue = (BYTE) round((float) blue / count);
        }
    }
    // copy image from dublicate
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = duplicate[i][j];
        }
    }
}
