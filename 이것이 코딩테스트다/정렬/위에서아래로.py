n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))

num.sort()
num.reverse()

# 한 줄로 합치기 => num=sorted(num,reverse=True)

for i in num:
    print(i,end=' ')