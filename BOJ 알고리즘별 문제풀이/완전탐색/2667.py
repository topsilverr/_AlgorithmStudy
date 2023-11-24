from collections import deque

n=int(input())
graph=[]
visited=[[0] * n for i in range(n)]
result=[]
for i in range(n):
    graph.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif graph[nx][ny] == 1 and visited[nx][ny]== 0 :
                visited[nx][ny] = 1
                queue.append((nx,ny))
                cnt+=1
    return cnt

result=[]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]==1:
            result.append(bfs(i,j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])