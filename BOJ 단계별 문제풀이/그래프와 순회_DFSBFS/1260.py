from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 문제 조건에서 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문한다고 함.
# => 한 정점에 연결된 정점들을 정렬하여 작은 수를 먼저 탐색하도록 해야함!
# => graph[i] 에 있는 값들 정렬하는 코드 필요
for i in range(1,n+1):
    graph[i].sort()

d_res=[] # dfs 의 결과 담기
b_res = [] # bfs 의 결과 담기
d_visited = [0] * (n + 1) # dfs 의 방문 확인
b_visited = [0] * (n+1) # bfs 의 방문 확인

def dfs(a):
    d_visited[a] = 1
    d_res.append(a)
    for i in graph[a]:
        if d_visited[i] == 0:
            dfs(i)


def bfs(b):
    queue=deque([b])
    b_visited[b]=1
    while queue:
        c=queue.popleft()
        b_res.append(c)
        for i in graph[c]:
            if b_visited[i] == 0 :
                queue.append(i)
                b_visited[i]=1

# 배열을 대괄호 없이 출력하기 => print(*(배열이름))
dfs(v)
print(*d_res)
bfs(v)
print(*b_res)
