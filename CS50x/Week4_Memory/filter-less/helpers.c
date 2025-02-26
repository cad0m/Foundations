#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    double avrg;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avrg = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0000);

            image[i][j].rgbtBlue = avrg;
            image[i][j].rgbtGreen = avrg;
            image[i][j].rgbtRed = avrg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sepiaaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            float sepiaaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            float sepiaaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaaRed > 255)
                sepiaaRed = 255;
            if (sepiaaGreen > 255)
                sepiaaGreen = 255;
            if (sepiaaBlue > 255)
                sepiaaBlue = 255;

            image[i][j].rgbtRed = sepiaaRed;
            image[i][j].rgbtGreen = sepiaaGreen;
            image[i][j].rgbtBlue = sepiaaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;

    for (int i = 0; i < height; i++)
    {
        int start = 0, end = width - 1;

        while (start < end)
        {
            tmp = image[i][start];
            image[i][start] = image[i][end];
            image[i][end] = tmp;
            start++;
            end--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE copie[height][width];

    //

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copie[i][j] = image[i][j];
        }
    }

    //
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //
            int count = 0;
            float filRed = 0, filGreen = 0, filBlue = 0;

            for (int m = i - 1; m < i + 2; m++)
            {
                if (m >= 0 && m < height)
                {
                    for (int n = j - 1; n < j + 2; n++)
                    {
                        if (n >= 0 && n < width)
                        {
                            filRed += copie[m][n].rgbtRed;
                            filGreen += copie[m][n].rgbtGreen;
                            filBlue += copie[m][n].rgbtBlue;
                            count++;
                        }
                    }
                }
            }
            image[i][j].rgbtRed = round(filRed / count);
            image[i][j].rgbtGreen = round(filGreen / count);
            image[i][j].rgbtBlue = round(filBlue / count);
        }
    }
    return;
}