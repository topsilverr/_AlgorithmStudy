from itertools import combinations

n = int(input())

graph = []
teacher = []
x = []
chk = 0

for _ in range(n):
    graph.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append([i, j])
        if graph[i][j] == 'X':
            x.append([i, j])

comb = list(combinations(x, 3))


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:  # [(1,1),(2,3),(4,2)]
        for k in range(4):
            px, py = t
            while 0 <= px < n and 0 <= py < n:
                if graph[px][py] == 'O':
                    break
                if graph[px][py] == 'S':
                    return False
                px += dx[k]
                py += dy[k]
    return True


for a, b, c in comb:
    graph[a[0]][a[1]] = 'O'
    graph[b[0]][b[1]] = 'O'
    graph[c[0]][c[1]] = 'O'

    res = bfs()

    if res:
        chk = 1

if chk == 1:
    print("YES")
else:
    print("NO")
