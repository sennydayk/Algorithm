# 해결 방안
# 1. 막대기 개수와 각각의 막대기 높이 입력받기
# 2. 입력받은 막대기 높이값을 스택에 추가
# 2-1. 스택이 비어 있으면 무조건 추가
# 2-2. 스택이 비어 있지 않고, 마지막 값이 입력값보다 작거나 같으면 마지막 값을 제거하고 추가
# 2-3. 스택이 비어 있지 않고, 마지막 값이 입력값보다 크면 제거하지 않고 추가
# 3. 스택에 남아 있는 높이값의 개수로 결과 도출

from sys import stdin
input = stdin.readline

N = int(input().strip())

# 막대기의 높이값을 저장할 스택 생성
stack = []

for _ in range(N):
    height = int(input().strip())

    # stack이 비어 있지 않고 stack 마지막 값이 입력값보다 작거나 같은 경우
    while stack and stack[-1] <= height:
        # stack의 마지막 값을 제거
        stack.pop()
    # 모든 경우에 입력값이 stack에 추가되므로 while문 밖에 작성
    stack.append(height)
    
print(len(stack))