s=input()
n=len(s)
a=[]
for i in range(n):
    if s[i]!='+':
        a.append(s[i])
a.sort()
for i in range(len(a)):
    if i==len(a)-1:
        print(a[i])
    else:
        print(a[i],end='+')