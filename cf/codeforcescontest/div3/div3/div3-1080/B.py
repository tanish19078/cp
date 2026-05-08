def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [0] + list(map(int, input().split()))  # 1-indexed

        # Build graph: edges i - 2i
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n // 2 + 1):
            adj[i].append(2 * i)
            adj[2 * i].append(i)

        visited = [False] * (n + 1)
        possible = True

        for i in range(1, n + 1):
            if not visited[i]:

                stack = [i]
                visited[i] = True
                comp = []
                while stack:
                    u = stack.pop()
                    comp.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)

                vals = [a[p] for p in comp]
                comp.sort()
                vals.sort()
                if comp != vals:
                    possible = False
                    break

        print("YES" if possible else "NO")
if __name__ == "__main__":
    solve()