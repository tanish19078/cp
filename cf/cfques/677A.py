n,h=map(int,input().split())
a=list(map(int,input().split()))
cw=0
cb=0
for i in a:
    if i>h:
        cb+=2
    else:
        cw+=1
print(cw+cb)