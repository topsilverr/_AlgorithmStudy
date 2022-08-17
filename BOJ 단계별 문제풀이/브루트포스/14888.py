from collections import deque
from itertools import permutations


n=int(input()) # 숫자 개수
a = list(map(int,input().split())) # 숫자 목록
s = list(map(int,input().split())) # 연산자 개수 ( +, -, x, / )

# 연산자 배열 만들기 by 순열 (itertools 라이브러리)
arr=[]

for x in range(0,4):
    if x == 0:
        for y in range(0,s[x]):
            arr.append('+')
    elif x == 1:
        for y in range(0,s[x]):
            arr.append('-')
    elif x == 2:
        for y in range(0,s[x]):
            arr.append('*')
    elif x == 3:
        for y in range(0,s[x]):
            arr.append('/')

result = list(permutations(arr,len(arr))) # 집합을 리스트 형식으로 변경 <= permutaions 사용하면 집합으로 반환됨
q=deque(result) # 큐를 사용하여 하나씩 꺼내서 계산

max_result=-1e9
min_result=1e9

while q:
    num=q.popleft() # 가능한 연산자 순열 수
    res=a[0]
    for i in range(1,len(a)):
        if num[i-1]=='+':
            res+=a[i]
        elif num[i-1]=='-':
            res-=a[i]
        elif num[i-1]=='*':
            res*=a[i]
        elif num[i-1]=='/':
            if res < 0 :
                res=-(abs(res)//a[i])
            else:
                res=res//a[i]

    max_result=max(max_result,res)
    min_result=min(min_result,res)

print(max_result)
print(min_result)









