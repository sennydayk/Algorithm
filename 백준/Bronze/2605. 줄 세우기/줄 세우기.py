# 리스트를 뒤집어서 생각한다.
# 1 뽑으면 1번째, 3 뽑으면 3번째에 서게 되므로 뽑은 숫자의 인덱스로 들어간다.
# 배열에서 특정 자리에 값을 삽입해주는 insert 함수 사용

n = int(input())

num_lst = list(map(int, input().split()))

std_lst = []

for i in range(n):
    std_lst.insert(num_lst[i], i+1)


std_lst = std_lst[::-1]
for x in std_lst:
    print(x, end=" ")

# 리스트 값을 꺼내는 다른 방법
#print(*std_list)