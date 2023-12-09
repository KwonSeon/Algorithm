import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

# print(N, M)

graph = [[] for _ in range(N + 1)]

# print(graph)

visited = [False] * (N + 1)

# print(visited)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

ans = 0


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
        # print(f"i:{i}, ans:{ans}")

print(ans)