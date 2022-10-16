from collections import deque

n, k = map(int, input().split())
time = 0

dx = [-1, 1, n]


def bfs(n, k):
    queue = deque()
    queue.append(n)
    global time
    time = 0
    while queue:
        n = queue.popleft()
        for i in range(3):
            nx = n + dx[i]
            if nx <= -1 or nx > 100000:
                continue
            elif nx == k:
                return time
            else:
                queue.append(nx)
                time += 1


bfs(n, k)
print(time)
