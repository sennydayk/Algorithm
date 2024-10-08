from sys import stdin
input = stdin.readline

n = int(input())
lst = [int(input()) for i in range(n)]

# 1. 평균
print(round(sum(lst)/n))

# 2. 중앙값
lst.sort()
print(lst[n // 2])

# 3. 최빈값
count = dict()
for i in lst:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
max_value = max(count.values())
max_lst = []

for i in count:
    if count[i] == max_value:
        max_lst.append(i)

if len(max_lst) == 1:
    print(max_lst[0])
else:
    print(max_lst[1])

# 4. 범위
print(max(lst) - min(lst))
