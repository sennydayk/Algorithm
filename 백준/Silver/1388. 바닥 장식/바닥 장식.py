# 입력
# 첫째 줄 : 방 바닥의 크기 (세로 N, 가로 M)
# 다음 N줄 : 바닥 장식 모양, - 와 | 이루어짐
# 두 개의 - 가 인접해 있고 같은 행에 있다면 같은 나무 판자로 간주
# 두 개의 | 가 인접해 있고 같은 열에 있다면 같은 나무 판자로 간주

# 출력
# 방 바닥을 장식하는 데 필요한 나무 판자 개수

# 해결 방안
# 각 행에서 -, 각 열에서 | 연속 여부를 확인
# 새로운 나무 판자를 찾을 때마다 판자 개수 카운트
# - : 왼쪽의 다른 -와 인접하지 않을 때 (이전에 판단한 판자의 일부가 아닐 때) 개수 카운트
# | : 위쪽의 다른 |와 인접하지 않을 때 (이전에 판단한 판자의 일부가 아닐 때) 개수 카운트


# 나무 판자를 카운트하는 함수 정의
def count_planks(N, M, floor):
    # 카운트 횟수 초기화
    count = 0
    
    # - 판자 카운트
    for i in range(N):
        for j in range(M):
            # - 판자 중 왼쪽 - 판자와 인접하지 않는 경우
            if floor[i][j] == '-' and (j == 0 or floor[i][j - 1] != '-'):
                # - 판자 개수 추가
                count += 1
    
    # | 판자 카운트
    for j in range(M):
        for i in range(N):
            # | 판자 중 위쪽 | 판자와 인접하지 않는 경우
            if floor[i][j] == '|' and (i == 0 or floor[i - 1][j] != '|'):
                # | 판자 개수 추가
                count += 1
    
    return count

# 입력받기
N, M = map(int, input().split()) 
floor = [input().strip() for _ in range(N)]

# 결과 출력
print(count_planks(N, M, floor))