n=int(input())
d=[100,20,10,5,1]
cnt=0
for i in d:
    cnt+=n//i
    n%=i
print(cnt)
