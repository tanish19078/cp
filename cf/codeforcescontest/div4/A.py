def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        result = [i * 2 for i in range(1, n + 1)]
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()