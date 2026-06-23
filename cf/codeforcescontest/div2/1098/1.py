t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    c0 = w.count(0)
    c1 = w.count(1)
    c2 = w.count(2)

    ans = c0 + min(c1, c2) + abs(c1 - c2) // 3
    print(ans)