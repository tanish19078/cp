def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    # Adjacency list
    adj = [
        [],
        [2,3,4,5],
        [1,3,4,6],
        [1,2,5,6],
        [1,2,5,6],
        [1,3,4,6],
        [2,3,4,5]
    ]
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        
        INF = 10**9
        dp_prev = [INF] * 7
        for v in range(1, 7):
            dp_prev[v] = 1 if a[0] != v else 0
        
        for i in range(1, n):
            dp_curr = [INF] * 7
            for v in range(1, 7):
                best = INF
                for u in adj[v]:
                    if dp_prev[u] < best:
                        best = dp_prev[u]
                dp_curr[v] = best + (1 if a[i] != v else 0)
            dp_prev = dp_curr
        
        ans = min(dp_prev[1:])
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()