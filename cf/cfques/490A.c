#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int prog[5000], math[5000], pe[5000];
    int p = 0, m = 0, e = 0;
    
    for (int i = 1; i <= n; i++) {
        int t;
        scanf("%d", &t);
        if (t == 1) prog[p++] = i;
        else if (t == 2) math[m++] = i;
        else pe[e++] = i;
    }
    // no of teams =min(p,m,e)
    int teams = p;
    if (teams > m) teams = m;
    if (teams > e) teams = e;
    
    printf("%d\n", teams);
    for (int i = 0; i < teams; i++) {
        printf("%d %d %d\n", prog[i], math[i], pe[i]);
    }
    
    return 0;
}