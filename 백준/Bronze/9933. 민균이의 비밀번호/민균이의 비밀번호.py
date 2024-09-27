from sys import stdin
input = stdin.readline

N = int(input())
words = []

for _ in range(N):
    word = input().rstrip()
    words.append(word)
    re_word = word[::-1]
    if re_word in words:
        print(len(word), end=" ")
        print(word[(len(word)-1)//2])