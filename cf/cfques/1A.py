n, m, a = map(int, input().split())
length = (n + a - 1) // a
width = (m + a - 1) // a
print(length * width)