# 해결 방안
# 1. 후보의 수와 각 후보를 뽑으려는 사람의 수 입력받기
# 2. 1번을 뽑으려는 사람의 수(v_1)는 따로 선언
# 3. 각 후보를 뽑으려는 사람의 수를 큰 순서대로 리스트 정렬 (votes)
# 4. 가장 큰 투표 수(votes[0]) 값이 v_1 값보다 크거나 같으면 votes[0] - 1(표 뺏기), v_1 + 1(뺏어오기) 수행
# 5. votes를 다시 내림차순으로 정렬
# 6. 4-5번 과정을 반복한 횟수가 결과값

N = int(input())
# 투표 수를 저장할 리스트 생성
votes = []
# 결과값으로 도출할 횟수를 초기화
count = 0

# 입력받은 후보별 투표 수를 votes에 추가
for i in range(N):
    votes.append(int(input()))

# 기호 1번의 투표 수를 변수로 선언
v_1 = votes[0]
# 기호 1번 투표 수는 리스트에서 제거
votes.pop(0)
# 투표 수 내림차순 정렬
votes.sort(reverse=True)

# 가장 큰 투표 수가 v_1보다 같거나 큰 경우 계속 반복
while votes and votes[0] >= v_1:
    # 가장 큰 투표 수 1 뺏기
    votes[0] -= 1
    # 기호 1번에게 뺏은 수 더해주기
    v_1 += 1
    # 리스트 내림차순으로 재정렬
    votes.sort(reverse=True)
    # 반복횟수 증가
    count += 1

print(count)