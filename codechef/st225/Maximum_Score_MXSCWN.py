# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    x=sum(arr1)
    mindf = float('inf')
    for i in range(n):
        d = arr1[i] - arr2[i]
        mindf = min(mindf, d)
    print(x-mindf)
    
