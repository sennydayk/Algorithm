# 입력
# 첫째 줄 : K (완전 이진 트리의 깊이)
# 둘째 줄 : 상근이가 방문한 빌딩 번호가 순서대로 주어짐

# 출력
# K개의 줄(노드의 레벨)에 걸쳐 출력
# 각 레벨별로 빌딩의 번호 출력

# 해결 방안
# 상근이의 빌딩 방문 순서는 중위 순회를 따름
# 빌딩 순서가 주어지므로, 각 방문 순서의 가운데 값이 root 노드가 된다.

from sys import stdin
input = stdin.readline

K = int(input())
# 상근이가 방문한 빌딩 순서를 리스트로 저장
orders = list(map(int, input().split()))
# 상근이가 방문한 빌딩 번호를 각각의 노드로 가지는 트리 생성
tree = [[] for _ in range(K)]

# 중위 순회 함수 생성 (배열과 level을 인자로 받음)
def inorder(arr, level):
    # 배열 중간값이 0레벨의 루트 노드일 것이므로 해당 인덱스값 mid에 할당
    mid = len(arr) // 2
    # 구한 0레벨 루트 노드값을 트리에 추가해주기
    tree[level].append(arr[mid])

    # 배열 원소가 1개가 되면 종료
    if len(arr) == 1:
        return
    # 중간값 기준 왼쪽 값들에 대해서 중위 순회 재귀 호출
    inorder(arr[:mid], level + 1)
    # 중간값 기준 오른쪽 값들에 대해서 중위 순회 재귀 호출
    inorder(arr[mid+1:], level + 1)

# 중위 순회 시작 (0레벨에서 시작)
inorder(orders, 0)

# 레벨 수만큼 반복하며 각 레벨에 있는 노드값 출력
for i in range(K):
    print(*tree[i])