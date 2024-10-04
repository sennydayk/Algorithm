# 입력
# 첫째 줄 : 배열의 길이 N
# 둘째 줄 : A 배열 원소
# 셋째 줄 : B 배열 원소

# 출력
# 각 원소를 곱한 값의 합(S)의 최소값

# 해결 방안
# A의 최소값은 B의 최대값과 곱해주고, 반대로 A의 최대값은 B의 최소값과 곱해주면 된다.
# B는 정렬을 사용할 수 없으므로 각 배열에서 최소 / 최대값을 구해 곱하고 제거하는 방식으로 구현

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0

for i in range(N):
    min_A = min(A)
    max_B = max(B)
    S += min_A * max_B
    A.pop(A.index(min_A))
    B.pop(B.index(max_B))

print(S)