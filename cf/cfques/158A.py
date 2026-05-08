a,b=map(int,input().split())
x=list(map(int,input().split()))
cnt=0
score=x[b-1]
for i in x:
    if i>=score and i>0:
        cnt+=1
print(cnt)
