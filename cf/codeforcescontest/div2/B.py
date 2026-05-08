import sys

def main():
    # Efficiently read input data
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        if idx >= len(data):
            break
        n = int(data[idx])
        x_str = data[idx+1]
        idx += 2
        
        ptr = 0
        possible = True
        
        # When n is odd, the first step (k=1) has n-k = odd length - 1 = even.
        # This means both the first and last characters are the same.
        # T_1 = 'a' and T_n = 'a' when n is odd. So S_1 must be 'a'.
        if n % 2 == 1:
            if x_str[0] == 'b':
                possible = False
            ptr = 1
            
        # Subsequent steps alternating between Odd (choice) and Even (forced).
        # In an Odd step k, we can choose S_k to be 'a' or 'b'. 
        # This choice then determines the character for the next Even step k+1.
        # Specifically, S_k and S_{k+1} must be different.
        if possible:
            while ptr < n:
                if ptr + 1 >= n:
                    # Should not happen given ptr increment and n check
                    break
                c1 = x_str[ptr]
                c2 = x_str[ptr+1]
                if c1 != '?' and c2 != '?' and c1 == c2:
                    possible = False
                    break
                ptr += 2
                
        results.append("YES" if possible else "NO")
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
