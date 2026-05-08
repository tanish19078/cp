import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    rows = N - K + 1
    cols = N - K + 1
    
    sums = [0] * (rows * cols)
    beauty = [0] * (N * N)
    current_max = 0
    
    out = []
    
    for _ in range(Q):
        r = int(data[idx]) - 1
        c = int(data[idx + 1]) - 1
        new_val = int(data[idx + 2])
        idx += 3
        
        pos_beauty = r * N + c
        inc = new_val - beauty[pos_beauty]
        beauty[pos_beauty] = new_val
        
        if inc == 0:
            out.append(str(current_max))
            continue
        
        start_i = r - K + 1
        if start_i < 0:
            start_i = 0
        end_i = r
        if end_i > rows - 1:
            end_i = rows - 1
        
        start_j = c - K + 1
        if start_j < 0:
            start_j = 0
        end_j = c
        if end_j > cols - 1:
            end_j = cols - 1
        
        for i in range(start_i, end_i + 1):
            base = i * cols
            for j in range(start_j, end_j + 1):
                pos = base + j
                sums[pos] += inc
                if sums[pos] > current_max:
                    current_max = sums[pos]
        
        out.append(str(current_max))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()