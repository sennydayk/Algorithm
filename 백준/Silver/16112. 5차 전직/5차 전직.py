n, k = map(int, input().split())
experience = list(map(int, input().split()))

experience.sort()
each_experience = 0
total_experience = 0

for i in range(n):
     total_experience += experience[i] * each_experience
     if each_experience < k:
          each_experience += 1

print(total_experience)