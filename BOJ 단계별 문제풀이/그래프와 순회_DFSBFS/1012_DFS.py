import sys
sys.setrecursionlimit(10000) # 재귀의 한도를 풀어주는 코드 <= 재귀함수를 이용해 풀 때에는 반드시 써주기

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    elif graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False


t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for k in range(m)]  # for 문으로 리스트 선언 => [[] * 세로 크기 for i in range( 가로 크기 )]
    cnt = 0
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for p in range(m):
        for q in range(n):
            if graph[p][q]==1:
                if dfs(p,q):
                    cnt+=1

    print(cnt)
