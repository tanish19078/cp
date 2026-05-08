#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    // even + even = even
    // odd + odd = even
    // check if w can be represented as sum of 2 even numbers or 2 odd numbers
        if(t > 2 && t% 2 == 0){
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }