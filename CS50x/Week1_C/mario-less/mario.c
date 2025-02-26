#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask for the height
    int height;
    do
    {
        height = get_int("give me the peramide height : ");
    }
    while (height < 1 || height > 8);
    // peramide
    int dots = height - 1;
    int sharps = height - dots;
    for (int i = 0 ; i < height; i++)
    {

        for (int j = 0 ; j < dots ; j++)
        {
            printf(" ");
        }
        for (int h = 0 ; h < sharps ; h++)
        {
            printf("#");
        }
        printf("\n");
        dots --;
        sharps++;
    }

}