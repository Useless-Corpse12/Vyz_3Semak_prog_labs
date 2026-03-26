from Lab10_2 import GraphVisual as EscapeFromLimb
from Lab10_1 import get_graf
#Хожу по рёбрам, делаю массив


def Bce_MocTbI(cnt, rts):

    adj = [[] for _ in range(cnt)]
    for edge in rts:
        u = edge[0] - 1  # → 0-based
        v = edge[1] - 1
        if 0 <= u < cnt and 0 <= v < cnt:
            adj[u].append(v)
            adj[v].append(u)

    tin = [-1] * cnt
    low = [-1] * cnt
    visited = [False] * cnt
    bridges = []
    timer = 0

    def dfs(v, parent):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1

        for to in adj[v]:
            if to == parent:
                continue
            if visited[to]:
                # обратное ребро
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                # условие моста
                if low[to] > tin[v]:
                    bridges.append((v, to))

    for v in range(cnt):
        if not visited[v]:
            dfs(v, -1)

    return [(u + 1, v + 1) for u, v in bridges]


rpaqpbl=["Graph.txt","GraphVes.txt","103Graph.txt"]
for ribbit in rpaqpbl:
    cnt,rts = get_graf(ribbit)
    EscapeFromLimb(cnt,rts)
    print(Bce_MocTbI(cnt,rts))