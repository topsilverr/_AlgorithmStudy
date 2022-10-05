from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

res=[]
b_res = []
def dfs(a):
    visited[a] = 1
    print(a,end=' ')
    for i in graph[a]:
        if visited[i] == 0:
            dfs(i)


def bfs(b):
    b_visited = [0] * (n+1)
    queue=deque([b])
    b_visited[b]=1
    while queue:
        c=queue.popleft()
        print(c, end=' ')
        for i in graph[c]:
            if b_visited[i] == 0 :
                queue.append(i)
                b_visited[i]=1

dfs(v)
print()
bfs(v)
