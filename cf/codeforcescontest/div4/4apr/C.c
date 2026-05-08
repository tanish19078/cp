#include <stdio.h>

int main() {
    int t;
    scanf("%d",&t);
    
    while(t--){
        int n;
        scanf("%d",&n);
        
        int l = 1;
        int r = 3*n;
        
        while(l <= n){
            printf("%d %d %d ", l, r-1, r);
            l++;
            r -= 2;
        }
        
        printf("\n");
    }
}