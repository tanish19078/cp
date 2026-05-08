import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        A = int(data[idx]); idx += 1
        B = int(data[idx]); idx += 1
        cA = int(data[idx]); idx += 1
        cB = int(data[idx]); idx += 1
        fA = int(data[idx]); idx += 1
        
        if A >= fA:
            out.append("0")
            continue
        
        def min_final_A(x):
            k_low = B // cB
            k_high = (B + x) // cB
            
            # k_low
            a_min = max(0, B + x - (k_low + 1) * cB + 1)
            if a_min > x:
                a_min = x
            val1 = A + a_min + k_low * cA
            
            # k_high
            a_min = max(0, B + x - (k_high + 1) * cB + 1)
            if a_min > x:
                a_min = x
            val2 = A + a_min + k_high * cA
            
            # k_high - 1 if in range
            best = min(val1, val2)
            if k_high - 1 >= k_low:
                a_min = max(0, B + x - k_high * cB + 1)
                if a_min > x:
                    a_min = x
                val3 = A + a_min + (k_high - 1) * cA
                best = min(best, val3)
            
            return best
        
        lo, hi = 0, 10**18
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if min_final_A(mid) >= fA:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        out.append(str(ans))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()