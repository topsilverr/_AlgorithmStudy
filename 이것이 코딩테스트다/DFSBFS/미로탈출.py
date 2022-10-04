from collections import deque

n,m = map(int,input().split())

road = []

for i in range(n):
    road.append(list(map(int,input())))

# 방향 설정 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >=m:
                continue
            elif road[nx][ny] == 0:
                continue
            elif road[nx][ny] == 1:
                road[nx][ny]=road[x][y]+1
                queue.append((nx,ny))
    return road[n-1][m-1]

res = bfs(0,0)
print(res)
