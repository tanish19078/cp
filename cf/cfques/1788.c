#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    
    while (t--) {
        int n;
        scanf("%d", &n);
        
        int arr[n];
        int totalTwos = 0;
        // since we only care about counting 2s, we can ignore other values

        // we just check index where left_2s = totalTwos/2, we don't need to store the whole array
        
        
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
            if (arr[i] == 2) {
                totalTwos++;
            }
        }
        
        // If odd number of 2s, impossible
        if (totalTwos % 2 != 0) {
            printf("-1\n");
            continue;
        }
        
        // Find smallest k where left_2s = totalTwos/2
        int target = totalTwos / 2;
        int leftTwos = 0;
        int k = -1;
        
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] == 2) {
                leftTwos++;
            }
            if (leftTwos == target) {
                k = i + 1;  // 1-indexed position
                break;
            }
        }
        
        printf("%d\n", k);
    }
    
    return 0;
}