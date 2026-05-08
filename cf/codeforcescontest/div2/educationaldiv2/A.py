t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())
    
    max_per_tower = d // m + 1
    
    if max_per_tower >= n:
        print(1)
    else:
        towers = (n + max_per_tower - 1) // max_per_tower
        print(towers)