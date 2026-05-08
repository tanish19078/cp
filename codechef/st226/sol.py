import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []

    for _ in range(T):
        N = int(data[idx]); idx += 1
        A = [int(data[idx + i]) for i in range(N)]
        idx += N

        mx = max(A)
        upper = 2 * mx

        pairs = []
        for i in range(N):
            v = A[i]
            while v <= upper:
                pairs.append((v, i))
                v *= 2

        pairs.sort()

        count = [0] * N
        covered = 0
        ans = float('inf')
        left = 0

        for right in range(len(pairs)):
            v, ei = pairs[right]
            if count[ei] == 0:
                covered += 1
            count[ei] += 1

            while covered == N:
                diff = v - pairs[left][0]
                if diff < ans:
                    ans = diff
                lei = pairs[left][1]
                count[lei] -= 1
                if count[lei] == 0:
                    covered -= 1
                left += 1

        out.append(str(ans))

    sys.stdout.write('\n'.join(out) + '\n')

solve()
