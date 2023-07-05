import sys
r,c = map(int,input().split())
alphas = set()
alp = []
for _ in range(r):
  alp.append(list(sys.stdin.readline()))

cnt = 0
px,py = 0,0
# x축이 세로(행)
# y축이 가로(열)
# 상 하 좌 우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,buf):
  global cnt

  cnt = max(cnt,buf)

  for i in range(4):
    px = x+dx[i]
    py = y+dy[i]

    if 0<= px < r and 0<= py < c and not alp[px][py] in alphas:
      alphas.add(alp[px][py])
      dfs(px,py,buf+1)
      alphas.remove(alp[px][py])


alphas.add(alp[0][0])
dfs(0,0,1)
print(cnt)