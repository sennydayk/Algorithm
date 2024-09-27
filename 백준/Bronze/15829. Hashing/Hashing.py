import string

r = 31
m = 1234567891

letters = list(string.ascii_lowercase)
nums = {}

for i in range(len(letters)):
    nums[letters[i]] = i+1

N = int(input())
str = input()
answer = 0
for i in range(N):
    answer += (nums[str[i]] * (r ** i)) % m

print(answer)