t=int(input())
for _ in range(t):
    N, K, Geff = map(int, input().split())
    masses = list(map(int, input().split()))
    
    left = max(masses)  
    right = sum(masses) 
    
    while left < right:
        mid = (left + right) // 2

        segments = 1
        current_weight = 0
        possible = True
        
        for m in masses:
            if m > mid:  
                possible = False
                break
                
            if current_weight + m > mid:
                segments += 1
                current_weight = m
                if segments > K:
                    possible = False
                    break
            else:
                current_weight += m
        
        if possible:
            right = mid
        else:
            left = mid + 1

    print(left * Geff)