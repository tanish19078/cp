x=int(input())
a=list(map(int,input().split()))
b=sorted(a)
# c=0
if b[-1]==1:
    print("HARD")
else:
    print("EASY")