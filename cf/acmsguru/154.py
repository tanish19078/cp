def zeros(n):
    cnt = 0
    while n:
        n //= 5
        cnt += n
    return cnt

def main():
    import sys
    Q = int(sys.stdin.readline().strip())

    lo, hi = 1, max(5, Q * 5 + 100)
    ans = -1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        z = zeros(mid)
        
        if z == Q:
            ans = mid
            hi = mid - 1
        elif z < Q:
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(ans if ans != -1 else "No solution")

if __name__ == "__main__":
    main()