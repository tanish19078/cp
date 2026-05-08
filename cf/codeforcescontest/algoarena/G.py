import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        L = int(input_data[idx]); idx += 1
        R = int(input_data[idx]); idx += 1
        arr = list(map(int, input_data[idx:idx+n])); idx += n
        
        MAX = max(arr)
        total_sum = sum(arr)
        
        # Frequency array
        freq = [0] * (MAX + 1)
        for x in arr:
            freq[x] += 1
        
        # Prefix sum of frequencies
        pref = [0] * (MAX + 2)
        for i in range(1, MAX + 2):
            pref[i] = pref[i-1] + freq[i]
        
        best = 0
        
        # For each k in [L, R]
        for k in range(L, R + 1):
            total_floor = 0
            # Sum over all multiples of k
            multiple = k
            q = 1
            while multiple <= MAX:
                cnt = pref[min(MAX, multiple + k - 1)] - pref[multiple - 1]
                total_floor += q * cnt
                q += 1
                multiple += k
            
            result = total_sum - k * total_floor
            if result > best:
                best = result
        
        out.append(str(best))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()