k, n, w = map(int, input().split())
total = 0
for i in range(1, w + 1):
    total += k * i

borrow = total - n
if borrow > 0:
    print(borrow)
else:
    print(0)