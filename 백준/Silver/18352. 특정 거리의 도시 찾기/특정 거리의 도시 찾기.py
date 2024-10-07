# 입력
# 첫째 줄 : N(도시의 개수), M(도로의 개수), K(거리 정보), X(출발도시의 번호)
# 다음 M줄 : 도시 번호 A, B (A, B 도시 사이 단방향 도로 존재)

# 출력
# 출발 도시 X로부터 최단 거리가 K인 도시 번호 (오름차순)
# 존재하지 않으면 -1 출력

from sys import stdin
from collections import deque
input = stdin.readline

N, M, K, X = map(int, input().split())
# 도시 개수만큼 리스트 생성 (도시 번호가 1부터이므로 N+1)
graph = [[] for _ in range(N+1)]
# 도로 정보를 graph에 저장
for _ in range(M):
    # 도시 a에서 도시 b로 이동하는 정보를 리스트에 추가
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 거리를 -1로 초기화 (출발이 0이므로)
distance = [-1] * (N+1)
# 출발 도시 거리는 자기 자신이므로 0
distance[X] = 0

# bfs 부분
# 큐가 빌 때까지 탐색
q = deque([X])
# 현재 도시를 pop
while q:
    now = q.popleft()
    # 현재 도시에서 연결된 도시 탐색
    for next_node in graph[now]:
        # 연결된 도시가 아직 방문하지 않은 도시라면
        if distance[next_node] == -1 :
            # 최단거리에 1을 더해서 갱신
            distance[next_node] = distance[now] + 1
            # 연결된 도시를 큐에 추가하여 다시 탐색할 수 있도록
            q.append(next_node)
# 최단거리 k를 충족하는 도시를 찾기 위한 check 선언
check = False
for i in range(1, N+1):
    # 모든 도시를 탐색하며 만약 최단거리가 k인 도시라면 
    if distance[i] == K:
        # 해당 도시 출력
        print(i)
        check = True
# check가 False면 k인 도시가 없는 것이므로 -1 출력
if check == False:
    print(-1)