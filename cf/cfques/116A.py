n = int(input())
current = 0
max_capacity = 0

for _ in range(n):
    a, b = map(int, input().split())
    current -= a
    current += b
    max_capacity = max(max_capacity, current)

print(max_capacity)