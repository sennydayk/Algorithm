from sys import stdin
from collections import deque

# 덱 정의
d = deque()
n = int(input())

# 입력받은 문자열을 공백 기준으로 나누어 리스트로 생성
for _ in range(n):
    command = stdin.readline().split()
		
		# 해당 command에 따른 명령 수행
    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
		        # print(d.popleft())가 안되는 이유 무엇? 런타임 에러 발생
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
        # >>> [TODO] if(len(deck) == 0):
		        # 마찬가지로 print(d.pop())는 런타임 에러 발생
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")