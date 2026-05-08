k=int(input())
def fib(k):
    if k <= 0:
        return 0
    elif k == 1:
        return 1

    a, b = 1, 1  
    total = 2    

    for i in range(3, k + 1):
        a, b = b, a + b
        total += b
    
    return total
print(fib(k))