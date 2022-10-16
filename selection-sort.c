#include <stdio.h>

int main(void) {
    int listed[] = {5, 19, 12, 5, 1, 21, 17, 23, 14};
    int len = sizeof(listed) / sizeof(int);
    for (int i = 0; i < len; i++) {
        int min = i;
        for (int j = i+1; j < len; j++) {
            if (listed[j] < listed[min]) {
                min = j;
            }
        }
        int new = listed[min];
        listed[min] = listed[i];
        listed[i] = new;
    }
    for (int k = 0; k < len; k++) {
        printf("%d ", listed[k]);
    }
}