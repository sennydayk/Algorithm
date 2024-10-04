# 입력
# 첫째 줄 : 단어의 개수 N
# 다음 N줄 : 단어들

# 출력
# 정렬된 단어 출력
# 1. 길이가 짧은 것부터
# 2.길이가 같으면 사전 순으로
# 중복 단어는 하나만 남기고 제거

from sys import stdin
input = stdin.readline

N = int(input())
words = []

for _ in range(N):
    words.append(input().strip())

words = list(set(words))
words.sort()
words.sort(key=len)

print(*words, sep='\n')