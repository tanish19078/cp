import sys

MOD = 10**9 + 7

def possible_quotients(x):
    res = []
    i = 1
    while i <= x:
        q = x // i
        res.append(q)
        i = x // q + 1
    return res

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1

        q_set = set()
        for q in possible_quotients(a):
            q_set.add(q)
        for q in possible_quotients(b):
            q_set.add(q)
        
        ans = 0
        for q in q_set:
            if q == 0:
                continue
            cntA = a // q - a // (q + 1)
            cntB = b // q - b // (q + 1)
            ans = (ans + cntA * cntB) % MOD
        
        out.append(str(ans))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()