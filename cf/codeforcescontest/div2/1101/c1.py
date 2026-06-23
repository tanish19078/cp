import sys

def main():
    eia = sys.stdin.buffer.read().split()
    p = 0
    t = int(eia[p]); p += 1
    out = []
    for _ in range(t):
        n,x,s = int(eia[p]),int(eia[p+1]),int(eia[p+2]); p += 3
        u = eia[p].decode(); p += 1
        sixseven = [-1]*(x+1); sixseven[0] = 0; mk = 0; cap = s-1
        for c in u:
            nxt = sixseven[:]; co = c!='E'; cj = c!='I'
            for k in range(min(mk,x)+1):
                j = sixseven[k]
                if j<0: continue
                if co and k<x and j>nxt[k+1]: nxt[k+1]=j
                if cj and j<k*cap and j+1>nxt[k]: nxt[k]=j+1
            if co: mk=min(mk+1,x)
            sixseven = nxt
        ans = max(k+sixseven[k] for k in range(x+1) if sixseven[k]>=0)
        out.append(str(ans))
    print('\n'.join(out))

main()