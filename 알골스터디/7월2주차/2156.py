import sys

input = sys.stdin.readline

n = int(input())

dp = [0]*10000

gr = [0]*10000

for i in range(n):
    gr[i] = int(input())

# 그리디,,,로 하면 안되나


dp[0] = gr[0]
dp[1] = gr[1] + dp[0]
dp[2] = max(gr[1]+gr[2], gr[0]+gr[2], dp[1])
for i in range(3,n):
    dp[i] = max(dp[i-2]+gr[i], dp[i-1], dp[i-3]+gr[i-1]+gr[i])

print(max(dp))



