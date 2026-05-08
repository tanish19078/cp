MAXN = 10**5
phi = list(range(MAXN + 1))
for i in range(2, MAXN + 1):
    if phi[i] == i:
        for j in range(i, MAXN + 1, i):
            phi[j] -= phi[j] // i

pref = [0] * (MAXN + 1)
for i in range(1, MAXN + 1):
    pref[i] = pref[i-1] + phi[i]

t = int(input())
for _ in range(t):
    n = int(input())
    total = 5 * n * (n + 1) // 2
    visible = 5 * pref[n]
    print(total - visible)