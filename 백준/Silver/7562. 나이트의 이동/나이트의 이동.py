from sys import stdin
from collections import deque
input = stdin.readline

dx = [-2, -2, 1, -1, 2, 2, 1, -1]
dy = [1, -1, -2, -2, 1, -1, 2, 2]

def bfs(cx, cy, gx, gy):
    count = 0
    q = deque()
    q.append((cx, cy, count))

    while q:
        x, y, count = q.popleft()
        if x == gx and y == gy:
            print(count)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))

T = int(input())
for _ in range(T):
    I = int(input())
    cx, cy = map(int, input().split())
    gx, gy = map(int, input().split())
    if cx == gx and cy == gy:
        print(0)
        continue
    board = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]

    bfs(cx, cy, gx, gy)