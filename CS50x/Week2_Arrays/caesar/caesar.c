#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // get the key
    if (argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (argv[1][i] < 48 || argv[1][i] > 57)
            {
                printf("Usage: ./caesar key  \n");
                return 1;
            }
        }
    }
    else
    {
        printf("Usage: ./caesar key \n");
        return 1;
    }
    // convert key
    int k = atoi(argv[1]);
    // plintext
    string ptext = get_string("plaintext:  ");
    // make the magic // print the text
    printf("ciphertext: ");
    for (int i = 0, n = strlen(ptext); i < n; i++)
    {
        if (isalpha(ptext[i]))
        {
            int m;
            if (islower(ptext[i]))
            {
                m = ptext[i] % 97;
                int ci = (m + k) % 26;
                printf("%c", 97 + ci);
            }
            else
            {
                m = ptext[i] % 65;
                int ci = (m + k) % 26;
                printf("%c", 65 + ci);
            }
        }
        else
        {
            printf("%c", ptext[i]);
        }
    }
    printf("\n");
    return 0;
}
