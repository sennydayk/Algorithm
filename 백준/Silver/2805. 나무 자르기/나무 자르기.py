from sys import stdin
input = stdin.readline

# 입력값 받기
n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 시작과 끝 값 설정
start, end = 1, max(lst) 

while start <= end:
    sum = 0
    # 중간값 설정
    mid = (start + end) // 2 

    # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산
    for l in lst:
        if l > mid:
            sum += l - mid  

    # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
    if sum < m:  
        # 높이를 낮춤
        end = mid - 1 
    # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같은 경우
    else:  
        # 높이를 높임
        start = mid + 1 

print(end)