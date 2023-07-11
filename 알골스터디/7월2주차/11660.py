import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0]*(n+1) for i in range(n+1)]


nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+nums[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])





# 파라미터 넣어서
#

# def memo_sum(x, y):
#     if x == 0 and y == 0:
#         return nums[x][y]
#     else:
#         if res[x][y] > 0:
#             return res[x][y]
#         else:
#             res[x][y] += memo_sum(x-1,y-1)
#             return res[x][y]
# # 1,3 까지
# memo_sum(0,2)
# res[0][2] += memo_sum(
# nums[0][2]
# 더하는 함수를 재귀로
# 각각 호출해서 빼기

# 2,1 에서 3,2
# if res[][] >0 and res[][]>0 :
#   return res[3][2] - res[2][1]
# else:
#   res32 +=