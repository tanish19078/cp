import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        k = int(input_data[idx]); idx += 1
        
        if k == 0 or k > 63:
            out.append("0")
            continue
        
        m = k - 1
        if n < (1 << m):
            out.append("0")
        else:
            ans = (n - (1 << m)) // (1 << (m + 1)) + 1
            out.append(str(ans))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()