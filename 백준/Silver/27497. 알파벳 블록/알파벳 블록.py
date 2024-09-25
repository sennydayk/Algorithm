from sys import stdin
from collections import deque

d = deque()
n = int(stdin.readline())
stack = []

for _ in range(n):
    command = list(map(str, stdin.readline().split()))
    if command[0] == '1':
        d.append(command[1])  
        stack.append('back')
    elif command[0] == '2':
        d.appendleft(command[1]) 
        stack.append('front')
    else:
        if stack:  
            value = stack.pop()
            if value == 'back':
                d.pop()  
            else:
                d.popleft()  


if len(d) == 0:
    print('0')
else:
    print("".join(d))