# 입력
# 첫째 줄 : 전체 사람의 수 n
# 둘째 줄 : 두 사람의 번호
# 셋째 줄 : 부모 자식 관계 개수 m

# 출력
# 두 사람의 촌수
# 촌수를 계산할 수 없다면 -1 출력

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

n=int(input())
A,B=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visited = [False] * (n + 1)
res=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(A)

if res[B]>0:
    print(res[B])
else:
    print(-1)