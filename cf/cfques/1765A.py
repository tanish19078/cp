t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        # Find the largest proper divisor
        d = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                d = n // i
                break
        print(d, n - d)