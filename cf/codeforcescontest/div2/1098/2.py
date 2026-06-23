t = int(input())

for _ in range(t):
    n, x1, x2, k = map(int, input().split())

    if n <= 3:
        print(1)
    else:
        d = abs(x1 - x2)
        d = min(d, n - d)
        print(d + k)