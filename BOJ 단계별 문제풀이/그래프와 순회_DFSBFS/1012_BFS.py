from collections import deque


def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=m or ny<=-1 or ny>=n:
                continue
            elif graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))


dx=[0,0,-1,1]
dy=[-1,1,0,0]

t = int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    graph = [[0] * n for k in range(m)] # for 문으로 리스트 선언 => [[] * 세로 크기 for i in range( 가로 크기 )]
    cnt=0
    for j in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1
    for p in range(m):
        for q in range(n):
            if graph[p][q]==1:
                bfs(p,q)
                cnt+=1
    print(cnt)
