# 해결 방안
# 1. 명령의 수와 각각의 명령 입력받기
# 2. 명령을 추가할 큐 생성
# 3. 명령에 해당하는 동작 실행
# 4. 명령을 수행한 결과값 곧바로 출력

from sys import stdin
input = stdin.readline

N = int(input())
q = []

for _ in range(N):
    command = input().split()

    # 해당 command에 따른 명령 수행
    # push
    if command[0] == "push":
        q.append(command[1])
    # pop
    elif command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            del q[0]
    # size
    elif command[0] == "size":
        print(len(q))
    # empty
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    # front
    elif command[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    # back
    elif command[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])