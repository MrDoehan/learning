#include <stdio.h>
#include <stdlib.h>
typedef struct node {
    int number;
    struct node *next;
}
node;

int main(void) {
    node *listed = NULL;
    node *n = malloc(sizeof(node));
    n->number = 1;
    n->next = NULL;
    listed = n;
    n = malloc(sizeof(node));
    n->number = 2;
    n->next = NULL;
    listed->next = n;
 
    n = malloc(sizeof(node));
    n->number = 5;
    n->next = NULL;
    listed->next->next = n; 
    for (node *tmp = listed; tmp != NULL; tmp = tmp->next) {
        printf("%d", tmp->number);
    }
}
