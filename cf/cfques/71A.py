n=int(input())
for i in range(n):
    a=input()
    x=len(a)
    if x>10:
        t=a[0]+str(x-2)+a[-1]
        print(t)
    else:
        print(a)