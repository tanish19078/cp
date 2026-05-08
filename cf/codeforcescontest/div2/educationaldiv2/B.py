def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        digits = [int(ch) for ch in s]
        total = sum(digits)
        
        if total <= 9:
            print(0)
            continue
        
        # Target sum ≤ 9
        target = 9
        
        # We need to reduce total by (total - 9)
        need_reduce = total - 9
        
        # Try reducing largest digits first (can reduce to 0 except first)
        reductions = []
        # First digit can't be 0, but can be reduced to 1-9
        if len(digits) > 1:
            for d in digits[1:]:
                reductions.append(d)  # can reduce to 0
            # First digit can reduce to 1 (max reduction = d-1)
            reductions.append(digits[0] - 1)
        
        # Sort reductions in descending order
        reductions.sort(reverse=True)
        
        moves = 0
        for r in reductions:
            need_reduce -= r
            moves += 1
            if need_reduce <= 0:
                break
        
        print(moves)