# 입력
# 첫째 줄 : N(정점의 수), M(간선의 수), R(시작 정점)
# 다음 M줄 : 간선 정보 u, v

# 출력
# 노드 방문 순서 출력
# i번째 줄에는 정점 i의 방문 순서
# 시작 정점에서 방문할 수 없는 경우 0 출력

from collections import deque
from sys import stdin
input = stdin.readline

N, M, R = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    count = 2

    while queue :
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=count
                count += 1

bfs(graph, R, visited)

for i in visited[1::]:
    print(i)