from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if grid[nx][ny] == 1:
                q.append((nx, ny))
                grid[nx][ny] = 0
    return

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    
    for i in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1
        
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                bfs(i, j)
                count += 1
                
    print(count)