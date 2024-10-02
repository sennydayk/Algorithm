# 입력
# 첫째 줄 : 영역의 크기 (R = 세로, C = 가로)
# 다음 R줄 : 영역의 정보 (. = 빈 공간, # = 울타리, v = 늑대, k = 양)

# 출력 : 살아남는 양과 늑대의 수

# 해결 방안
# 울타리로 둘러싸인 영역을 파악
# 영역 내부에 있는 양과 늑대의 수를 비교해서 계산
# dfs로 풀어보기

from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)] 
visited = [[False] * C for _ in range(R)] 

def dfs(x, y) :
    global sheep, wolf
    visited[x][y] = True
    if graph[x][y] == 'v':
        wolf += 1
    if graph[x][y] == 'k':
        sheep += 1
    
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '#':
            dfs(nx, ny)

total_sheep, total_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            sheep, wolf = 0, 0
            dfs(i, j)

            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)