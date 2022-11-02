x=int(input())


# 이렇게 하면 5 나옴 -> 최소 횟수가 아님!
# cnt=0
# while x!=1:
#     if x%5==0:
#         x=x/5
#         cnt+=1
#     elif x%3==0:
#         x=x/3
#         cnt+=1
#     elif x%2==0:
#         x=x/2
#         cnt+=1
#     else:
#         x=x-1
#         cnt+=1
#
# print(cnt)

# DP 사용
d=[0]*30001

for i in range(2,x+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)

print(d[x])