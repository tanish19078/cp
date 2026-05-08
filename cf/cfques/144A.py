n = int(input())
a = list(map(int, input().split()))

max_val = max(a)
min_val = min(a)

max_index = a.index(max_val)  # first occurrence from left
min_index = n - 1 - a[::-1].index(min_val)  # last occurrence from right

swaps = max_index + (n - 1 - min_index)
if max_index > min_index:
    swaps -= 1

print(swaps)