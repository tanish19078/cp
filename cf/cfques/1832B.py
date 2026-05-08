#include <stdio.h>
#include <math.h>

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, k;
        scanf("%d %d", &n, &k);
        int a[n];
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
// Sort the array using bubble sort
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
        for (int i = 0; i < k; i++){
            if (a[0]+a[1] > a[n-1]){
                arr.pop
            }
            else
                break;
        }