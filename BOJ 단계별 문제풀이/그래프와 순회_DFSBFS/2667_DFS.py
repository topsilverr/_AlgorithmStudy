n=int(input())
graph=[]
visited=[[0] * n for i in range(n)]
result=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    elif graph[x][y]==1 and visited[x][y]==0:
        visited[x][y]=1
        global cnt
        cnt+=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

apt=0
cnt=0
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            result.append(cnt)
            apt+=1
            cnt=0

result.sort()
print(apt)
for i in range(len(result)):
    print(result[i])

