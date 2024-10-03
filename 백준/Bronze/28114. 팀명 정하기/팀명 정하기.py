# 입력
# 첫째 줄 : 1번 팀원의 정보 (P1 = 문제수, Y2 = 연도, S1 = 성씨)
# 둘째 줄 : 2번 팀원의 정보 (P2, Y2, S2)
# 셋째 줄 : 3번 팀원의 정보 (P3, Y3, S3)

# 출력
# 첫째 줄 : 학번을 오름차순으로 정렬한 팀명
# 둘째 줄 : 문제 수가 많은 순서대로 성씨 첫 글자를 나열한 팀명

# 해결 방안

from sys import stdin
input = stdin.readline

years = []
problems = []

for i in range(3):
    p, y, s = input().split()
    years.append(int(y) % 100)
    problems.append([int(p), s])

years.sort()
problems.sort(reverse=True)

first_teamname = ''
second_teamname = ''

for j in range(3):
    first_teamname += str(years[j])
    second_teamname += problems[j][1][0]

print(first_teamname)
print(second_teamname)