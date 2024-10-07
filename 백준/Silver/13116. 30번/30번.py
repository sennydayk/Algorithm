# 두 노드가 공통으로 포함하는 루트 노드 구하기

from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    while True:
        # 두 노드의 부모 노드가 같으면
        if a == b:
            # 부모 노드의 10배를 출력
            print(a * 10)
            break

        # a가 더 클 경우 a의 부모 노드
        if a > b:
            a //= 2

        # b가 더 클 경우 b의 부모 노드
        else:
            b //= 2