#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while(t--) {
        int n;
        scanf("%d", &n);

        int temp = n;
        int digits = 0;

        // count digits
        while(temp > 0) {
            digits++;
            temp /= 10;
        }

        // find first digit
        int first = n;
        while(first >= 10) {
            first /= 10;
        }

        int result = (digits - 1) * 9 + first;

        printf("%d\n", result);
    }

    return 0;
}