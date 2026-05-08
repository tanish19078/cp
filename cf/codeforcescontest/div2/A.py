import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t_str = input_data[idx]
    t = int(t_str)
    idx += 1
    
    results = []
    for _ in range(t):
        if idx + 1 >= len(input_data):
            break
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        # Logic: 
        # x = 2*a + 3*b + 4*c
        # y = a - c  => a = y + c
        # Substituting: x = 2*(y + c) + 3*b + 4*c = 2*y + 3*b + 6*c
        # x-2y = 3*(b + 2*c)
        # We need non-negative integers a, b, c.
        # a = y + c >= 0  => c >= max(0, -y)
        # b = (x - 2*y)/3 - 2*c >= 0 => 2*c <= (x - 2*y)/3 => c <= (x - 2*y)/6
        # So we need an integer c in [max(0, -y), (x - 2*y)/6]
        # This interval is non-empty if max(0, -y) <= (x - 2*y)/6
        # and (x - 2*y) must be divisible by 3.
        
        k = x - 2 * y
        if k >= 0 and k % 3 == 0:
            if y >= 0:
                # max(0, -y) = 0, so 0 <= k/6 is always true for k >= 0
                results.append("YES")
            else:
                # max(0, -y) = -y, so -y <= k/6 => -6y <= x - 2y => x >= -4y
                if x >= -4 * y:
                    results.append("YES")
                else:
                    results.append("NO")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
