# 입력
# 첫 번째 줄 : 인구수 N, 센티의 키 H, 뿅망치 횟수 제한 T
# 다음 N줄 : 각 거인의 키 H

# 출력
# 첫 번째 줄 : 전략 성공 여부(YES/NO)
# 두 번째 줄 : 뿅망치를 최소로 사용한 횟수

import heapq

N, H, T = map(int, input().split())

# 거인의 키를 저장할 힙 생성
heights = []

# 입력값을 음수로 변환해서 힙에 추가 (최대힙으로 구현)
for _ in range(N):
    heapq.heappush(heights, -int(input()))

# 횟수 초기화
count = 0

for _ in range(T):
    if -heights[0] != 1 and -heights[0] >= H:
        heapq.heapreplace(heights, -(-heights[0] // 2))
        count += 1

    
if -heights[0] < H:
    print("YES")
    print(count)
else:
    print("NO")
    print(-heights[0])