n = int(input())
arr = list(map(int, input().split()))

even_count = 0
odd_count = 0
last_even_index = 0
last_odd_index = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even_count += 1
        last_even_index = i + 1
    else:
        odd_count += 1
        last_odd_index = i + 1

if even_count == 1:
    print(last_even_index)
else:
    print(last_odd_index)