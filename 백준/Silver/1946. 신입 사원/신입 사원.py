# 입력
# 첫째 줄 : 테스트 케이스 T
# 각 케이스 첫째 줄 : 지원자의 숫자 N
# 다음 N줄 : 서류 성적, 면접 성적

# 출력
# 채용할 수 있는 최대 신입사원 수

# 해결 방안
# 다른 사람보다 적어도 하나의 점수는 높아야 채용할 수 있다.
# 일단 서류 점수로 정렬했을 때 점수가 가장 높은 지원자는 무조건 뽑힌다.
# 서류 점수 2등부터는, 서류 점수 1등의 면접 점수보다 높아야 뽑힌다.
# 즉, 서류 점수 i등 지원자는 i-1등 지원자들보다 면접 점수가 높아야 뽑힌다.

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = []
    for _ in range(N):
        rank.append(list(map(int, input().split())))
    rank.sort()
    best = rank[0][1]
    count = 1
    for i in range(N):
        if best > rank[i][1]:
            best = rank[i][1]
            count += 1
    print(count)