S = input()
result = set()
for i in range(len(S)):
    for sub_set in range(i, len(S)):
        result.add(S[i:sub_set+1])
print(len(result))