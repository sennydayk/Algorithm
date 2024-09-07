N, M = input().split()
N, M = int(N), int(M)

origin_bun = []

for i in range(N):
  origin_bun.append(input())

for reverse_bun in origin_bun:
  print(reverse_bun[::-1])