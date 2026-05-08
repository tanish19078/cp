N, M = map(int, input().split())
S = set(input().strip())
T = set(input().strip())
Q = int(input())

for _ in range(Q):
    word = set(input().strip())
    
    if word.issubset(S) and not word.issubset(T):
        print("Takahashi")
    elif word.issubset(T) and not word.issubset(S):
        print("Aoki")
    else:
        print("Unknown")