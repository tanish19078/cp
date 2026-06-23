n = int(input())
m = []

for i in range(n):
    a, b = map(int, input().split())
    m.append((b, a))

m.sort()

ans = 0
t = 0

for i, j in m:
    if j >= t:
        ans += 1
        t = i

print(ans)