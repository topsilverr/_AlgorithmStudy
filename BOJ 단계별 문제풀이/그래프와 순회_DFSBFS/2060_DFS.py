n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 정보 수
# 양방향 그래프 사용.... => graph=[[]for i in range(n+1)]
graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[0]*(n+1)

def dfs(x):
    visited[x]=1
    for i in graph[x]:
        if visited[i]==0:
            dfs(i)


dfs(1)
print(sum(visited)-1)