n,m,k=map(int,input().split())
a=list(map(int,input().split())) #desired
b=list(map(int,input().split())) #actually present
#x-k to x+k is limit
a.sort()
b.sort()
i=j=0
ans=0
while i<n and j<m:
    if b[j]<a[i]-k:
        j+=1
    elif b[j]>a[i]+k:
        i+=1
    else:
        i+=1
        j+=1
        ans+=1
print(ans)