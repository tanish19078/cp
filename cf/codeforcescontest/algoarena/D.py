import sys
import heapq

def solve():
    input_data = sys.stdin.buffer.read().split()
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        k = int(input_data[idx]); idx += 1
        arr = list(map(int, input_data[idx:idx+n])); idx += n
        
        heap = []
        total_sq = 0
        total_abs = 0
        for val in arr:
            total_sq += val * val
            mag = abs(val)
            total_abs += mag
            if mag > 0:
                gain = 2 * mag - 1 
                heapq.heappush(heap, (-gain, mag))
        
        if k <= total_abs:

            for _ in range(k):
                if not heap:
                    break
                neg_gain, mag = heapq.heappop(heap)
                gain = -neg_gain
                total_sq -= mag * mag
                new_mag = mag - 1
                total_sq += new_mag * new_mag
                if new_mag > 0:
                    new_gain = 2 * new_mag - 1
                    heapq.heappush(heap, (-new_gain, new_mag))
        else:

            total_sq = 0  
            leftover = k - total_abs

            total_sq = leftover % 2
        
        out.append(str(total_sq))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()