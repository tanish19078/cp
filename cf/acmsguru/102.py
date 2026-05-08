import math
N=int(input())
def count_coprime_generator(N):
    return sum(1 for i in range(1, N + 1) if math.gcd(i, N) == 1)
print(count_coprime_generator(N))