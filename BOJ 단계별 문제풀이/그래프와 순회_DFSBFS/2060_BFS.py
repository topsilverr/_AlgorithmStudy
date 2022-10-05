from collections import deque

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 정보 수
# 양방향 그래프 사용.... => graph=[[]for i in range(n+1)]
graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)



# bfs 사용!

def bfs():
    visited = [0] * (n + 1)
    queue = deque([1]) # queue에 1번 넣기
    visited[1] = 1  # 1번 컴퓨터 방문 표시
    cnt=0
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                cnt+=1
    return cnt

print(bfs())