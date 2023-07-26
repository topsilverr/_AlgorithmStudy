import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

s = []

for _ in range(n):
    s.append(int(input()))

l, r = 0, 0
cnt = 0
buf_cnt = 0
set_li = []
while r != n:
    buf_li = []
    buf = 0
    buf_r = r
    for i in range(k):
        if r <= n-k: # 원 돌아가기 전
            l = r + i
            buf_li.append(s[l])
        else: # 다시 0으로 돌아갈 수 있으니까,,,
            l = buf_r % n
            buf_r += 1
            buf_li.append(s[l])
    set_li = set(buf_li)
    if len(set_li) == len(buf_li) and c not in buf_li:
        buf_cnt = k + 1
        cnt = max(buf_cnt,cnt)
        break # 최댓값 나오면 break
    elif len(set_li) == len(buf_li) and c in buf_li:
        buf_cnt = k
        cnt = max(buf_cnt,cnt)
    elif len(set_li) != len(buf_li) and c not in buf_li:
        buf_cnt = len(set_li) + 1
        cnt = max(buf_cnt,cnt)
    elif len(set_li) != len(buf_li) and c in buf_li:
        buf_cnt = len(set_li)
        cnt = max(buf_cnt,cnt)

    r += 1 # r 이 기준,,,

print(cnt)


# 4567
#
# r = 5 i = 0123
# 5670
# l = r % n

# r = 6
# 6701
#
# r = 7
# 7012
# l = r+i