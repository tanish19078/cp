t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    a=list(input().strip())
    ops=[]

    for i in range(1,n//2+1):
        l=0
        for j in range(n-i):
            if a[j]=="1":
                l=j+1
                s[j]="0" if s[j]=="1" else "1"
                s[j+i]="0" if s[j+i]=="1" else "1"
                break
            ops.append(str(l)
        res.append(" ".join(ops))
print("\n".join(res))


