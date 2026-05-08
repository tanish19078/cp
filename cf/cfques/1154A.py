x = list(map(int, input().split()))
max_val = max(x)
for num in x:
    if num != max_val:
        print(max_val - num, end=' ')
print()