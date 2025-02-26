#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int main(void)
{
    // ay zeki
    string text = get_string("text : ");
// tfa7a hihi
    float L, W, S;
    W = count_words(text);
    L = count_letters(text) / W * 100;
    S = count_sentences(text) / W * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
// banana
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index));
    }


}
//-----------------------------------
int count_letters(string text)
{
    int count = 0;
    for (int i = 0 ; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}
//-----------------------------------
int count_words(string text)
{
    int count = 1;
    for (int i = 0 ; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            count++;
        }
    }
    return count;
}
//-----------------------------------
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0 ; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}