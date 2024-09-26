# 해결 방안
# 1. 전체 케이스 개수와 각 케이스 입력받기
# 2. 각 케이스를 공백을 기준으로 잘라 리스트에 추가
# 3. 리스트 순서를 뒤집기
# 4. "Case #x:" 형태로 결과값 출력

from sys import stdin
input = stdin.readline

N = int(input())

for i in range(N) :
    # 2
    case = list(input().split())
    # 3
    case = case[::-1]
    # 4
    print(f"Case #{i+1}:", *case) 

    # *case는 case 리스트 내 모든 원소를 대괄호 없이 출력