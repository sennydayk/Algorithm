# 해결 방안
# 1. 후보의 수와 각 후보를 뽑으려는 사람의 수 입력받기
# 2. 1번을 뽑으려는 사람의 수(v_1)는 따로 선언
# 3. 각 후보를 뽑으려는 사람의 수를 큰 순서대로 리스트 정렬 (votes)
# 4. votes내 값(votes[i])을 순회하면서 v_1보다 크거나 같으면 votes[i]에 -1, v_1에는 +1 해주기 반복
# 5. v_1이 votes[i]보다 크면 votes[i] 제거
# 6. 4번 과정을 반복한 횟수가 결과값

N = int(input())
votes = []
count = 0

for i in range(N):
    votes.append(int(input()))

v_1 = votes[0]
votes.pop(0)
votes.sort(reverse=True)

while votes and votes[0] >= v_1:
    votes[0] -= 1
    v_1 += 1
    count += 1
    votes.sort(reverse=True)

print(count)