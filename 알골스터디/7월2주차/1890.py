import sys

input = sys.stdin.readline

n = int(input())

game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

dp = [[0] * n for i in range(n)]
res = 0

dp[0][0] = 1

# dp[n-1][n-1] 을 구하는 것
for i in range(n):
    for j in range(n):
        if game[i][j] == 0:
            continue
        if j+game[i][j] < n:
            dp[i][j+game[i][j]] += dp[i][j]
        if i+game[i][j] < n:
            dp[i+game[i][j]][j] += dp[i][j]

print(dp[n-1][n-1])




