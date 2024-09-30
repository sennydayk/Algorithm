# 입력
# 첫째 줄 : R(행), C(열)
# 둘째 줄부터 : R개의 행과 C개의 열로 구성된 그리드 내 각 줄 입력받기
# #(잔디), .(잔디 X), 상하좌우로 인접한 #은 하나의 잔디로 간주

# 출력
# 잔디의 개수

# 해결 방안
# dfs(깊이 우선 탐색) 함수 이용
# dfs 함수는 상하좌우로 인접한 #를 모두 탐색하여 하나의 잔디로 간주
# 전체 농장을 순회하면서 #를 탐색하고 개수 증가

# dfs 탐색을 위한 방향 설정
# 행 인덱스 변화 (상, 하)
dx = [-1, 1, 0, 0]
# 열 인덱스 변화 (좌, 우)
dy = [0, 0, -1, 1]

# 깊이 우선 함수 정의
def dfs(x, y, field, visited, R, C):
    # 시작 좌표 초기화 (스택으로 생성)
    stack = [(x, y)]
    # 해당 위치를 방문한 것으로 표시
    visited[x][y] = True

    # 스택에 탐색할 셀이 있는 동안 반복
    while stack:
        # 스택 마지막 요소(현재 좌표)를 가져와 처리
        cx, cy = stack.pop()

        # 현재 좌표에서 가능한 네 방향을 모두 확인 (상하좌우)
        for i in range(4):
            # 인접한 좌표를 계산
            nx, ny = cx + dx[i], cy + dy[i]
            # (nx, ny) 좌표가 경계 내에 있고, 방문하지 않은 좌표이며, #이 포함된 경우
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] == '#':
                # 방문한 좌표로 표시하고
                visited[nx][ny] = True
                # 스택에 추가
                stack.append((nx, ny))

# 잔디 개수를 카운트하는 함수 정의
def count_grass(R, C, field):
    visited = [[False] * C for _ in range(R)]
    count = 0

    # 각 좌표를 탐색하기 위해 이중포문 수행
    for i in range(R):
        for j in range(C):
            # 잔디가 포함되어 있고 방문하지 않은 좌표인 경우 (즉 잔대가 발견된 경우)
            if field[i][j] == '#' and not visited[i][j]:
                # dfs 호출
                dfs(i, j, field, visited, R, C)
                # 횟수 증가
                count += 1

    return count

# 입력받기
R, C = map(int, input().split())
field = [input().strip() for _ in range(R)]

# 결과값 계산
result = count_grass(R, C, field)
print(result)