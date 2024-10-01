from sys import stdin
import heapq
input = stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    answer = 0

    while len(files) > 1:
        a, b = heapq.heappop(files), heapq.heappop(files)
        expense = a + b
        answer += expense
        heapq.heappush(files, expense)
    print(answer)