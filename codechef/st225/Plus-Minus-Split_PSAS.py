T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    found = False
    for i in range(N):
        v = A[i]
        ok = True
        for j in range(N):
            if j < i:
                if A[j] != -v:
                    ok = False
                    break
            else:
                if A[j] != v:
                    ok = False
                    break
        if ok:
            found = True
            break
    print("YES" if found else "NO")

# The operation zeros out position i while adding A[i] to everything before and subtracting from everything after. 
# The key insight: the only reachable "all equal" state is all zeros,
#  and you can only get there in one shot if the array is shaped like [-v, -v, ..., -v, v, v, ..., v] 
# — a block of -v followed by a block of v. 
# So we just check every possible split point to see if that two-block pattern exists.