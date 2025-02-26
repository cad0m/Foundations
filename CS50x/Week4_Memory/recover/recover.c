#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("not opend :( %s.\n", argv[1]);
        return 1;
    }

    BYTE buffer[512];
    char FilName[8]; //  store filename

    FILE *img = NULL; // Initialize file pointer
    int count = 0;

    while (fread(buffer, 1, 512, raw_file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xe0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }

            sprintf(FilName, "%03i.jpg", count);
            img = fopen(FilName, "w");
            if (img == NULL)
            {
                fclose(raw_file);
                return 1;
            }

            fwrite(buffer, 1, 512, img);
            count++;
        }
        else if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    if (img != NULL)
    {
        fclose(img);
    }

    fclose(raw_file);
    return 0;
}