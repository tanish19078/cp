#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    
    while (t--) {
        int n;
        scanf("%d", &n);
        
        int totalXor = 0;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            totalXor ^= x;
        }
        
        if (n % 2 == 1) {
            // n odd: x = totalXor always works
            printf("%d\n", totalXor);
        } else {
            // n even: works only if totalXor == 0
            if (totalXor == 0) {
                printf("%d\n", 0);
            } else {
                printf("%d\n", -1);
            }
        }
    }
    
    return 0;
}