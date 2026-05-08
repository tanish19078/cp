#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        if(n==67){
            printf("%d\n",67);
        }
        else{
            printf("%d\n",n+1);
        }
    }
}