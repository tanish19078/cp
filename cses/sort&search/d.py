import sys

input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(a[i], i + 1) for i in range(n)]
arr.sort()

i, j = 0, n - 1

while i < j:
    s = arr[i][0] + arr[j][0]

    if s == x:
        print(arr[i][1], arr[j][1])
        break
    elif s < x:
        i += 1
    else:
        j -= 1
else:
    print("IMPOSSIBLE")