n = int(input())

arrival = []
departure = []

for _ in range(n):
    a, b = map(int, input().split())
    arrival.append(a)
    departure.append(b)

arrival.sort()
departure.sort()

i = j = 0
cur = ans = 0

while i < n:
    if arrival[i] < departure[j]:
        cur += 1
        ans = max(ans, cur)
        i += 1
    else:
        cur -= 1
        j += 1

print(ans)