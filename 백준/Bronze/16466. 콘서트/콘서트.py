from sys import stdin
input = stdin.readline

N = int(input())
tickets = list(map(int, input().split()))
tickets.sort()

for i in range(N):
    if tickets[i] != i+1:
        print(i+1)
        break
if tickets[-1] == N:
    print(N+1)