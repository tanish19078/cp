t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    if x[0] != x[1] and x[0] != x[2]:
        print(1)
    elif x[1] != x[0] and x[1] != x[2]:
        print(2)
    else:
        for i in range(2, n):
            if x[i] != x[0]:
                print(i + 1)
                break
