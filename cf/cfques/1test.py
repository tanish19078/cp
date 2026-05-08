t=int(input())
mod=998244353
import math
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if a.sort()==a:
        for i in range(n):
            if a[i]