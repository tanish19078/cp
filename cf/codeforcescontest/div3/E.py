import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out_lines = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = list(map(int, data[idx:idx+n])); idx += n
        
        # Differences and their positions
        diff_positions = [[] for _ in range(n)]  # diff d -> list of positions i where diff[i]=d
        for i in range(n-1):
            d = abs(p[i] - p[i+1])
            diff_positions[d].append(i)
        
        # Initially all subarrays are exquisite for k=1
        total = n * (n + 1) // 2
        res = []
        
        # We start with k=1: all subarrays valid
        # For k from 1 to n-1, before output for k, we must have removed bad pairs with diff < k
        # Actually we compute for k=1 separately, then adjust
        
        # We'll simulate by adding bad positions as k increases
        # Use a list to store current segments as intervals [l, r]
        # Initially one segment [0, n-1]
        segments = [(0, n-1)]
        seg_counts = { (0, n-1): total }
        
        # For each k from 1 to n-1
        for k in range(1, n):
            # Add new bad positions with diff = k-1
            for pos in diff_positions[k-1]:
                # Find segment containing pos
                for seg in segments:
                    l, r = seg
                    if l <= pos < r:
                        # Split at pos
                        segments.remove((l, r))
                        old_cnt = (r-l+1)*(r-l+2)//2
                        total -= old_cnt
                        # New segments: [l, pos] and [pos+1, r]
                        if l <= pos:
                            seg1 = (l, pos)
                            cnt1 = (pos-l+1)*(pos-l+2)//2
                            segments.append(seg1)
                            total += cnt1
                        if pos+1 <= r:
                            seg2 = (pos+1, r)
                            cnt2 = (r-pos)*(r-pos+1)//2
                            segments.append(seg2)
                            total += cnt2
                        break
            res.append(str(total))
        
        out_lines.append(" ".join(res))
    
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()