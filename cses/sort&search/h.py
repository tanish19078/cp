import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

tickets.sort()

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def upper_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l

for x in customers:
    idx = find(upper_bound(tickets, x))

    if idx == 0:
        print(-1)
    else:
        print(tickets[idx - 1])
        parent[idx] = find(idx - 1)