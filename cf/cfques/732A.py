k,r=map(int,input().split())
for n in range(1,11):
    if (k*n)%10==r or (k*n)%10==0:
        print(n)
        break
    