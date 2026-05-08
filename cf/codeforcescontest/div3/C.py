import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    iterator = iter(data)
    try:
        t_cases = int(next(iterator))
    except StopIteration:
        return
        
    results = []
    
    for _ in range(t_cases):
        try:
            n = int(next(iterator))
            k = int(next(iterator))
        except StopIteration:
            break
            
        # Case 1: Target is larger than source
        if k > n:
            results.append("-1")
            continue
            
        # Case 2: Target is already the source size
        if k == n:
            results.append("0")
            continue
            
        found_time = -1
        p = 1      # This represents 2^time
        time = 0
        
        # Iterate through depths (time)
        # Since n <= 10^9, time will not exceed ~30. 
        # Loop breaks when piles become too small.
        while True:
            time += 1
            p *= 2
            
            # Calculate base pile size (quotient) and remainder
            q = n // p
            r = n % p
            
            # At this depth, we have:
            # - 'r' piles of size (q + 1)
            # - 'p - r' piles of size q
            
            # Check if k exists in the current set of piles
            match = False
            if r > 0:
                # We have both sizes: q and q+1
                if k == q or k == q + 1:
                    match = True
                current_max = q + 1
            else:
                # We only have size q
                if k == q:
                    match = True
                current_max = q
            
            if match:
                found_time = time
                break

            if current_max < k:
                break
        
        results.append(str(found_time))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()