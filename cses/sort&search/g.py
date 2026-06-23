n = int(input())
a = list(map(int, input().split()))

a.sort()
median = a[n // 2]

ans = 0
for x in a:
    ans += abs(x - median)

print(ans)