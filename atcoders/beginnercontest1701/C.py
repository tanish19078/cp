import sys

def solve():
    data = sys.stdin.read().split()
    N, K, X = int(data[0]), int(data[1]), int(data[2])
    A = list(map(int, data[3:3+N]))

    A.sort(reverse=True)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    ans = -1
    for m in range(1, N + 1):
        s = m - (N - K)
        if s <= 0:
            continue
        
        worst_sake = prefix[m] - prefix[m - s]
        if worst_sake >= X:
            ans = m
            break
    
    print(ans)

if __name__ == "__main__":
    solve()