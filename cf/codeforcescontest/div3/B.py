import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        s = int(data[idx]); idx += 1
        k = int(data[idx]); idx += 1
        m = int(data[idx]); idx += 1
        
        if m < k:
            ans = max(0, s - m)
        else:
            q = m // k
            r = m % k
            if s <= k:
                ans = max(0, s - r)
            else:
                if q % 2 == 0:
                    ans = max(0, s - r)
                else:
                    ans = max(0, k - r)
        out.append(str(ans))
    
    print("\n".join(out))

if __name__ == "__main__":
    solve()