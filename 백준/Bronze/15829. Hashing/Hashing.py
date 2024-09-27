# 해결 방안
# 1. 단어 리스트 생성
# 2. 알파벳을 key, 알파벳을 숫자로 변환한 값을 value로 가지는 쌍을 딕셔너리에 추가
# 3. 문자열 길이, 문자 입력받기
# 4. 문제에서 제시한 연산 수행하여 결과값 도출

r = 31
m = 1234567891

# 알파벳 리스트 생성
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 숫자로 변환한 값을 추가해줄 딕셔너리 선언
nums = {}

# letters 리스트 내 문자를 key, 문자 인덱스 + 1 값을 value로 가지도록 num에 추가
for i in range(len(letters)):
    nums[letters[i]] = i+1

# 사용자 입력
N = int(input())
str = input()
# 답 초기화
answer = 0
# 입력받은 문자 길이만큼 반복하면서 연산 수행
for i in range(N):
    answer += (nums[str[i]] * (r ** i)) % m
    
# for문 밖에서 연산 수행
answer %= m
print(answer)