import sys
input = sys.stdin.readline

sixseven = int(input())
for _ in range(sixseven):
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = n
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        ans = min(ans, max(i, n - j))
        i = j
    print(ans)