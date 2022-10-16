#include <stdio.h>
int main(void) {
    int x = 0;
    int y = x+1;
    int listed[] = {x, y};
    for (int i = 2; i < 20; i++) {
        listed[i] = listed[i-1] + listed[i-2];
    }
    for (int k = 0; k < 20; k++) {
        printf("%d\n", listed[k]);
    }
}