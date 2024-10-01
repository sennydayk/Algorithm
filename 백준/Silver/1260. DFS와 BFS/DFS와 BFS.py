N, M, V = map(int, input().split())

# 그래프 생성
graph = [[0] * (N + 1) for _ in range(N + 1)]

# 간선 정보 입력
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 기록 초기화
visited_bfs = [0] * (N + 1)
visited_dfs = [0] * (N + 1)

# DFS 함수 (스택 사용)
def dfs(V):
    stack = [V]
    while stack:
        node = stack.pop()
        if visited_dfs[node] == 0:
            visited_dfs[node] = 1
            print(node, end=" ")
            for n in range(N, 0, -1):
                if graph[node][n] == 1 and visited_dfs[n] == 0:
                    stack.append(n)

# DFS 함수 (재귀 사용)
def dfs_재귀(V):
    visited_dfs[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited_dfs[i] == 0:
            dfs_재귀(i)

# BFS 함수
def bfs(V):
    queue = [V]
    visited_bfs[V] = 1
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for i in range(1, N + 1):
            if graph[node][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1

# DFS 실행
dfs(V)
print()

# 방문 기록 초기화 후 BFS 실행
visited_dfs = [0] * (N + 1)
bfs(V)