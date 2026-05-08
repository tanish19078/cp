x=int(input())
s=input()
cnt=0
for i in range(1,x):
    if s[i]==s[i-1]:
        cnt+=1
print(cnt)
    
