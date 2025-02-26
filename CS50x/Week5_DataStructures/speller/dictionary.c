// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;
// Word counter
int counter = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hushnum = hash(word);
    node *tmp = table[hushnum];
    while (tmp != NULL)
    {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int index1 = tolower(word[0]) - 'a';
    int index2 = (strlen(word) > 1) ? (tolower(word[1]) - 'a') : 0;
    return index1 * 26 + index2;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    // open dictionary
    char klma[LENGTH + 1];
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("could not open");
        return false;
    }
    while (fscanf(file, "%s", klma) != EOF)
    {
        counter++;
        int hushnum = hash(klma);
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("no space");
            return false;
        }
        strcpy(n->word, klma);
        n->next = NULL;
        n->next = table[hushnum];
        table[hushnum] = n;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i];
            table[i] = tmp->next;
            free(tmp);
        }
    }
    return true;
}
