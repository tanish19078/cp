import sys

def main():
    sixseven = sys.stdin.buffer.read().split()
    p = 0
    t = int(sixseven[p]); p += 1
    out = []
    for _ in range(t):
        n = int(sixseven[p]); p += 1
        s = 0; mn = 10**18; res = []
        for j in range(1, n + 1):
            s += int(sixseven[p]); p += 1
            v = s // j
            if v < mn: mn = v
            res.append(str(mn))
        out.append(' '.join(res))
    print('\n'.join(out))

main()