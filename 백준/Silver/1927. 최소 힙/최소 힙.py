# 입력
# 첫째 줄 : 연산의 개수 N개
# 다음 N개의 줄 : 연산 정보를 나타내는 x
# x가 자연수면 배열에 추가, x가 0이면 배열 최소값 출력 후 제거

# 출력
# 0이 주어진 횟수만큼 연산 결과를 출력

# 해결 방안
# heapq 라이브러리 사용하기
# heappop(heap) : heap에서 가장 작은 원소 삭제 후 그 값 리턴
# heappush(heap, x) : heap에 x 원소 추가

from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

# 힙 생성
heap = []

N = int(input())

for _ in range(N):
    x = int(input())

    # x가 0인 경우
    if x == 0 :
        # heap에 원소가 존재하지 않으면 0을 출력
        if len(heap) == 0:
            print(0)
        # heap에서 가장 작은 원소 제거하고 출력
        else:
            print(heappop(heap))
    # x가 자연수인 경우 heap에 x 추가
    else:
        heappush(heap, x)