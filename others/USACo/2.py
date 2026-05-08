import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    k = int(data[1])
    idx = 2
    out_lines = []

    for _ in range(t):
        N = int(data[idx]); idx += 1
        S = data[idx].decode(); idx += 1

        # Check if each character appears an even number of times
        if (S.count('C') % 2 != 0 or
            S.count('O') % 2 != 0 or
            S.count('W') % 2 != 0):
            out_lines.append("-1")
            continue

        n = len(S)
        # Get positions of each character
        posC = [i for i, ch in enumerate(S) if ch == 'C']
        posO = [i for i, ch in enumerate(S) if ch == 'O']
        posW = [i for i, ch in enumerate(S) if ch == 'W']

        # Create pairs by matching first with last, second with second-last, etc.
        pairs = []
        for lst in (posC, posO, posW):
            m = len(lst)
            for j in range(m // 2):
                pairs.append((lst[j], lst[m - 1 - j]))

        # Check if one operation is possible: max(left) < min(right)
        if pairs:
            max_left = max(p[0] for p in pairs)
            min_right = min(p[1] for p in pairs)
            if max_left < min_right:
                # One operation suffices
                out_lines.append("1")
                out_lines.append(" ".join(["1"] * n))
                continue

        # Otherwise, two operations are needed (or three if k=1)
        M = 2
        if k == 1:
            M = 3

        # Assign pairs to two groups based on left index
        pairs.sort(key=lambda x: x[0])
        mid = len(pairs) // 2
        ops = [0] * n
        for i, (l, r) in enumerate(pairs):
            op = 1 if i < mid else 2
            ops[l] = op
            ops[r] = op

        out_lines.append(str(M))
        out_lines.append(" ".join(map(str, ops)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()