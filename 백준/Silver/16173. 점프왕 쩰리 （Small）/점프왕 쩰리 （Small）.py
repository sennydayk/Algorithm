# 입력
# 첫째 줄 : N(게임 구역의 크기)
# 다음 N줄 : 맵
# 승리 지점(오른쪽 맨 아래)는 -1, 나머지에는 0 이상 100 이하의 정수

# 출력
# 쩰리가 끝에 도달하면 HaruHaru, 도달할 수 없으면 Hing

# 해결 방안
# bfs(너비 우선 탐색) 사용
# 쩰리가 이동할 수 있는 모든 위치를 탐색하기 위한 큐 생성

from collections import deque

# 쩰리의 성공 여부를 판단하는 함수
def can_jellie_win(N, game_board):
    # 큐를 시작 지점인 (0,0)으로 초기화
    queue = deque([(0, 0)])
    # 방문한 지점을 추적하기 위한 집합 생성 (중복 방문 방지 위함)
    visited = set()
    visited.add((0, 0))
    
    # 쩰리는 오른쪽과 아래 방향으로만 이동 가능하므로 이동 방향을 두 가지로 정의
    directions = [(0, 1), (1, 0)]
    
    # BFS exploration
    while queue:
        x, y = queue.popleft()
        
        # 쩰리가 -1 지점에 도달하면 승리
        if game_board[x][y] == -1:
            return "HaruHaru"
        
        # 현재 위치에서 이동할 수 있는 단계 가져오기
        step = game_board[x][y]
        
        # 만약 이동할 수 없는 경우, 현재 위치 초기화
        if step == 0:
            continue
        
        # 가능한 이동 지점 좌표 탐색
        for dx, dy in directions:
            nx, ny = x + dx * step, y + dy * step
            # 해당 좌표가 방문하지 않은 지점인 경우
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                # visited, queue에 좌표 추가
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    # -1 지점에 도달하지 못한 경우 패배
    return "Hing"

# 입력받기
N = int(input()) 
game_board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(can_jellie_win(N, game_board))