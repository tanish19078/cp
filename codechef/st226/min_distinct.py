import sys
from collections import Counter

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []

    for _ in range(T):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        A = [int(data[idx + i]) for i in range(N)]
        idx += N

        first_val = A[0]
        freq = Counter(A)

        # A[0]'s value can never be eliminated (position 1 can't be overwritten)
        freq.pop(first_val)

        # Sort remaining value frequencies ascending
        others = sorted(freq.values())

        distinct = len(others) + 1  # +1 for A[0]'s value which always stays

        remaining_k = K
        for f in others:
            if remaining_k >= f:
                remaining_k -= f
                distinct -= 1
            else:
                break

        out.append(str(distinct))

    sys.stdout.write('\n'.join(out) + '\n')

solve()
