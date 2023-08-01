# heapq 사용
import sys,heapq

input = sys.stdin.readline

n = int(input())

cls = []
endTime = []

for _ in range(n):
    cls.append(list(map(int, input().split())))

cls.sort()

# 가장 작은 값이 index 0번에 저장됨
heapq.heappush(endTime,cls[0][1])
res = 1 # 전체 강의실 개수

for i in range(1,n):
    if cls[i][0] < endTime[0]:
        res+=1
        heapq.heappush(endTime,cls[i][1])
    else:
        heapq.heappop(endTime) # index 0번 pop, 즉 삭제
        heapq.heappush(endTime,cls[i][1])

print(res)