#include <stdio.h>

int main() {
    int t;
    scanf("%d",&t);
    
    while(t--){
        int a[7];
        int sum = 0;
        int max = -100;
        
        for(int i=0;i<7;i++){
            scanf("%d",&a[i]);
            sum += a[i];
            if(a[i] > max){
                max = a[i];
            }
        }
        
        int ans = -sum + 2*max;
        printf("%d\n", ans);
    }
}