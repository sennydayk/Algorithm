# 입력
# 첫번째 줄 : 테스트 케이스
# 각 테스트 케이스의 첫번째 줄 : 의상의 수 n개
# 다음 n개에 의상 이름, 의상 종류가 공백으로 구분되어 주어짐

# 출력
# 의상을 입을 수 있는 경우의 수

# 해결 방안
# 의상 종류가 여러 개여도 1개의 종류만 입어도 된다.
# 즉 옷으로 조합할 수 있는 모든 경우의 수에서 아무것도 안 입는 경우를 빼주면 된다.
# 예를 들어 (a종류 개수 + 1) * (b종류 개수 + 1) - 1 형태로 구할 수 있다.
# 의상 종류를 key, 종류별 의상 개수를 value로 가지는 딕셔너리를 생성해서 값에 접근한다.

from sys import stdin
input = stdin.readline

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 의상 종류의 개수를 저장할 딕셔너리 생성
    cloth = {}
    # 각 케이스마다 의상의 수 입력
    n = int(input())

    # 의상 이름, 종류를 각각 변수로 저장
    for _ in range(n):
        name, type = input().split()
        # 딕셔너리에 종류별 의상 개수 카운트
        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1
    
    # 결과값 초기화
    result = 1
    # 딕셔너리 내에 있는 value값들을 모두 곱해주기
    for i in cloth:
        result *= (cloth[i] + 1)

    # 전체 경우의 수에서 1 빼주기
    print(result - 1)