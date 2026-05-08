#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int arr[n];
        for (int i=0; i<n; i++) {
            scanf("%d", &arr[i]);
        }
    // sort array 
    for (int i=0;i<n;i++){
        for (int j=0;j<n-i-1;j++){
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    int p=1;
    for (int i=1; i<n; i++) {
        if (arr[i] -arr[i-1] > 1) {
            p=0;
            break;
        }
    }
    if (p) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    }
}
