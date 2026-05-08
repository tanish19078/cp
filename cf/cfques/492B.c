#include <stdio.h>

int main() {
    int n, l;
    scanf("%d %d", &n, &l);
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    
    // Sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    
    // Max gap between consecutive lanterns
    double max_gap = 0;
    for (int i = 1; i < n; i++) {
        double gap = a[i] - a[i - 1];
        if (gap > max_gap) max_gap = gap;
    }
    
    // Edges
    double d = a[0];
    if (l - a[n - 1] > d) d = l - a[n - 1];
    if (max_gap / 2.0 > d) d = max_gap / 2.0;
    
    printf("%.10f\n", d);
    return 0;
}