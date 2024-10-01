from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
std = deque()
max_std = 0
last_std = None

for _ in range(n):
    input_list = list(map(int, input().split()))
    type = input_list[0]

    if type == 1: 
        num = input_list[1]
        std.append(num)
        
        if len(std) > max_std:
            max_std = len(std)
            last_std = num 
        elif len(std) == max_std:
            last_std = min(last_std, num) 

    elif std and type == 2:  
        std.popleft()

        if len(std) == max_std and std:
            last_std = std[-1] 

print(max_std, last_std)