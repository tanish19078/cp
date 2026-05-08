n=int(input())
a=["I hate", "I love"]
for i in range(n):
    print(a[i%2], end="")
    if i!=n-1:
        print(" that ", end="")
    else:
        print(" it")
        