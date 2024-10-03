# 입력
# 첫째 줄 : 테스트 케이스 T
# 각 T별 첫째 줄 : 학교의 수 N
# 다음 N줄 : 학교 이름, 술의 양

# 출력
# 각 테스트마다 소비한 술의 양이 가장 많은 학교의 이름

# 해결 방안
# [학교 이름, 술의 양]을 원소로 가지는 이중배열 만들기
# 술의 양을 key로 내림차순 정렬
# 리스트 첫 번째 원소의 첫 번째 원소 출력

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    # 학교 정보를 저장할 리스트 생성
    univ = []
    for _ in range(N):
        # 학교별 정보 리스트로 생성
        info = list(input().split())
        # 두 번째 요소(술의 양) 정수 변환
        info[1] = int(info[1])
        # univ 리스트에 추가
        univ.append(info)
    # 술의 양을 key로 내림차순 정렬
    univ.sort(key=lambda x: -x[1])
    # 결과 출력
    print(univ[0][0])