t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=sorted(a)

    if k>1 or a==b:
        print("YES")
    else:
        print("NO")
    