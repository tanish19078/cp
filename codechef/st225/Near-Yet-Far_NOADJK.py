import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if K == 2:
        odd_vals = [A[i] for i in range(0, N, 2)]
        even_vals = [A[i] for i in range(1, N, 2)]
        ans = max(odd_vals) - min(odd_vals) if len(odd_vals) > 1 else 0
        if len(even_vals) > 1:
            ans = max(ans, max(even_vals) - min(even_vals))
        print(ans)
    else:
        if N <= 2:
            print(0)
            continue
        indices = list(range(N))
        indices.sort(key=lambda i: A[i])
        bot3 = indices[:min(3, N)]
        top3 = indices[-min(3, N):]
        ans = 0
        for mi in bot3:
            for ma in top3:
                if abs(ma - mi) >= 2:
                    val = A[ma] - A[mi]
                    if val > ans:
                        ans = val
        print(ans)

# We want the max difference (max − min) among elements we pick, with spacing constraints.
# K = 2: The rules force us into exactly two rigid sequences — odd-indexed or even-indexed elements. We just compute the range (max − min) of each group and take the better one.
# K ≥ 3: The spacing is flexible enough that any two non-adjacent elements can coexist in a valid sequence. So we grab the 3 largest and 3 smallest values, try all 9 pairs, and pick the best pair that's at least 2 positions apart