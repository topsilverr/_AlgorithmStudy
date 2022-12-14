# 집합 자료형 사용

n = int(input())

# 집합 자료형에 기록
items = set(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

for t in target:
    if t in items:
        print('yes',end=' ')
    else:
        print('no',end=' ')