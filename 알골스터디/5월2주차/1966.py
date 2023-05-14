from collections import deque
import sys

t = int(input())

res = []

for _ in range(t):
    n,m = map(int,input().split())
    deq = deque(list(map(int,sys.stdin.readline().split())))
    tar_list = deque(list(range(n)))
    cnt = 0

    while deq:
        if max(deq) != deq[0]:
            deq.append(deq.popleft())
            tar_list.append(tar_list.popleft())
        else:
            cnt += 1
            deq.popleft()
            if tar_list.popleft()== m:
                print(cnt)