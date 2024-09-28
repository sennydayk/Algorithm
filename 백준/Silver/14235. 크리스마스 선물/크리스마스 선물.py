# 입력
# 첫 번째 줄 : 방문 횟수 n
# 다음 n줄 - 거점지 방문 : 충전한 선물의 개수와 각 선물의 가치 입력
#          아이들 만남 : 0 입력

# 출력
# 입력이 0일 때마다 아이들에게 준 선물의 가치 출력
# 선물이 없다면 - 1 출력

# 해결 방안
# 선물의 가치를 저장하는 힙 생성
# 아이들을 만날 때마다 가장 큰 가치의 선물을 주어야 하므로 최대 힙으로 구현
# 

from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

# 선물의 가치를 저장할 힙 생성
max_value = []

# 방문 횟수 입력받기
n = int(input())

for _ in range(n):
    # 입력값 a 받기
    a = input().rstrip()
    # a가 0인 경우 (문자열로 비교)
    if a == '0' :
        # 선물이 없으면 -1 출력
        if len(max_value) == 0:
            print(-1)
        # 힙에서 최소값 제거 후, 양수로 변환해서 최대값으로 출력
        else:
            print(-heappop(max_value))
    # a가 0이 아닌 경우
    else :
        # 입력받은 a를 공백으로 구분해 리스트로 저장
        values = list(map(int, a.split()))
        # 리스트의 첫 번째 값은 선물의 개수이므로 가치와 무관하니까 제거
        values.pop(0)
        # 최대 힙 구현을 위해 음수로 변환하여 max_value에 저장
        for value in values:
            heappush(max_value, -value)