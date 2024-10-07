# 입력
# n(정점의 수), m(간선의 수), r(시작 정점)

# 출력
# 정점 i의 방문 순서 출력
# 시작 정점 방문 순서는 1, 방문할 수 없는 경우 0

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력값 받기
n, m, r = map(int, input().split())
# 그래프 생성
graph = [[] for _ in range(n+1)]
# 방문 순서 저장할 리스트 생성 (순서를 저장해야 하므로 0 초기값)
visited = [0] * (n+1)

count = 1
def dfs(graph, v, visited):
    global count
    visited[v] = count 
    
    for i in graph[v]:
        # 방문을 하지 않은 노드인 경우
        if visited[i] == 0:
            # 카운트 증가
            count += 1
            # dfs 재귀 호출
            dfs(graph, i, visited)
            
# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# 오름차순 정렬
for i in range(n+1):
    graph[i].sort()

dfs(graph, r, visited)

# 순차 출력
for i in range(1, n+1):
    print(visited[i])