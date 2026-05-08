def solve():
    import sys
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        f = [0] + list(map(int, data[idx:idx+n])); idx += n  
        
        S = (f[1] + f[n]) // (n - 1) 
        
        p = [0] * (n + 1)  
        for x in range(1, n):
            p[x] = (f[x+1] - f[x] + S) // 2
        
        a = [0] * (n + 1)
        a[1] = p[1]
        for i in range(2, n):
            a[i] = p[i] - p[i-1]
        a[n] = S - p[n-1]
        
        out_lines.append(' '.join(map(str, a[1:])))
    
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()