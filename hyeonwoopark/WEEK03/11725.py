# 백준 11725 트리의 부모 찾기

# 내가 한 거 (뎁스 땜에 시간초과 : 인접리스트로 바꾸기 귀찮)
# import sys
# sys.setrecursionlimit(10000)

# n = int(sys.stdin.readline())
# graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# visited = [False for _ in range(n + 1)]
# parents = [-1 for _ in range(n + 1)]

# for i in range(n - 1):
#     u, v = map(int, sys.stdin.readline().strip().split(" "))
#     graph[u][v] = 1
#     graph[v][u] = 1

# def dfs(st):
#     visited[st] = True

#     for i in range(1, n + 1):
#         if graph[st][i] == 0 or visited[i]:
#             continue
#         else:
#             parents[i] = st
#             dfs(i)

# dfs(1)
# for i in range(2, n + 1):
#     print(parents[i])

# 인접리스트로
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)


if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    parent = [0] * (n+1)

    while True:
        try:
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        except:
            break

    for i in range(n+1):
        graph[i].sort()

    dfs(1)

    print(*parent[2:], sep='\n')