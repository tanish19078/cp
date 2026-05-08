def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def solve():
    N, K = map(int, input().split())
    count = 0
    for i in range(1, N + 1):
        if digit_sum(i) == K:
            count += 1
    print(count)

if __name__ == "__main__":
    solve()