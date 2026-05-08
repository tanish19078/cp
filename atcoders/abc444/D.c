#include <stdio.h>
#include <stdlib.h>

#define MAX_A 200005

int main(void) {
    int N;
    scanf("%d", &N);
    
    int* A = malloc(N * sizeof(int));
    int max_A = 0;
    int freq[MAX_A + 1] = {0};
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
        freq[A[i]]++;
        if (A[i] > max_A) max_A = A[i];
    }
    
    int size = max_A + 10;
    int* digits = calloc(size, sizeof(int));
    
    for (int k = 0; k <= max_A; k++) {
        digits[k] = freq[k];
    }
    
    for (int k = 0; k < size - 1; k++) {
        digits[k + 1] += digits[k] / 10;
        digits[k] %= 10;
    }
    
    int borrow = N;
    for (int k = 0; k < size && borrow > 0; k++) {
        int b = borrow % 10;
        digits[k] -= b;
        borrow /= 10;
        if (digits[k] < 0) {
            digits[k] += 10;
            borrow++;
        }
    }
    
    int start = size - 1;
    while (start >= 0 && digits[start] == 0) start--;
    
    if (start < 0) {
        printf("0\n");
    } else {
        int rem = 0;
        for (int k = start; k >= 0; k--) {
            int val = rem * 10 + digits[k];
            digits[k] = val / 9;
            rem = val % 9;
        }
        
        while (start >= 0 && digits[start] == 0) start--;
        if (start < 0) {
            printf("0\n");
        } else {
            for (int k = start; k >= 0; k--) {
                printf("%d", digits[k]);
            }
            printf("\n");
        }
    }
    
    free(A);
    free(digits);
    return 0;
}