import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n = 열개수(가로) m = 행개수(세로)

board = [[0 for i in range(m)] for j in range(n)]

qList = list(map(int, input().split()))
kList = list(map(int, input().split()))
pList = list(map(int, input().split()))

q = qList[0]
k = kList[0]
p = pList[0]

if q:
    for i in range(q):
        board[qList[i * 2 + 1] - 1][qList[i * 2 + 2] - 1] = 'q'

if k:
    for i in range(k):
        board[kList[i * 2 + 1] - 1][kList[i * 2 + 2] - 1] = 'k'

if p:
    for i in range(p):
        board[pList[i * 2 + 1] - 1][pList[i * 2 + 2] - 1] = 'p'

# 나이트 확인
if k:
    for i in range(k):
        x = kList[i * 2 + 1] - 1
        y = kList[i * 2 + 2] - 1

        # x-1 y-2
        if x - 1 >= 0 and y - 2 >= 0:
            if board[x - 1][y - 2] == 0:
                board[x - 1][y - 2] = 'u'
        # x-1 y+2
        if x - 1 >= 0 and y + 2 < n:
            if board[x - 1][y + 2] == 0:
                board[x - 1][y + 2] = 'u'
        # x+1 y-2
        if x + 1 < m and y - 2 >= 0:
            if board[x + 1][y - 2] == 0:
                board[x + 1][y - 2] = 'u'
        # x+1 y+2
        if x + 1 < m and y + 2 < n:
            if board[x + 1][y + 2] == 0:
                board[x + 1][y + 2] = 'u'
        # x-2 y-1
        if x - 2 >= 0 and y - 1 >= 0:
            if board[x - 2][y - 1] == 0:
                board[x - 2][y - 1] = 'u'
        # x-2 y+1
        if x - 2 >= 0 and y + 1 < n:
            if board[x - 2][y + 1] == 0:
                board[x - 2][y + 1] = 'u'
        # x+2 y-1
        if x + 2 < m and y - 1 >= 0:
            if board[x + 2][y - 1] == 0:
                board[x + 2][y - 1] = 'u'
        # x+2 y+1
        if x + 2 < m and y + 1 < n:
            if board[x + 2][y + 1] == 0:
                board[x + 2][y + 1] = 'u'

# 퀸 확인
if q:
    for i in range(q):
        x = qList[i * 2 + 1] - 1
        y = qList[i * 2 + 2] - 1

        ld = 1
        # 왼쪽 대각선
        while True:
            if x-ld>=0 and y-ld>=0:
                if board[x-ld][y-ld] == 0 or board[x-ld][y-ld] == 'u':
                    board[x-ld][y-ld] = 'u'
                    ld += 1
                elif board[x-ld][y-ld] == 'q' or board[x-ld][y-ld] == 'p' or board[x-ld][y-ld] == 'k':
                    break
            else:
                break

        rd = 1
        while True:
            if x+rd<m and y+rd<n:
                if board[x+rd][y+rd] == 0 or board[x+rd][y+rd] == 'u':
                    board[x+rd][y+rd] = 'u'
                    rd += 1
                elif board[x+rd][y+rd] == 'q' or board[x+rd][y+rd] == 'p' or board[x+rd][y+rd] == 'k':
                    break
            else:
                break
        # 오른쪽 대각선

        rd = 1
        while True:
            if x-rd>=0 and y+rd<n:
                if board[x-rd][y+rd] == 0 or board[x-rd][y+rd] == 'u':
                    board[x-rd][y+rd] = 'u'
                    rd += 1
                elif board[x-rd][y+rd] == 'q' or board[x-rd][y+rd] == 'p' or board[x-rd][y+rd] == 'k':
                    break
            else:
                break

        ld = 1
        while True:
            if x+ld<m and y-ld>=0:
                if board[x+ld][y-ld] == 0 or board[x+ld][y-ld] == 'u':
                    board[x+ld][y-ld] = 'u'
                    ld += 1
                elif board[x+ld][y-ld] == 'q' or board[x+ld][y-ld] == 'p' or board[x+ld][y-ld] == 'k':
                    break
            else:
                break
        # 위

        u = 1
        while True:
            if x-u>=0:
                if board[x-u][y] == 0 or board[x-u][y] == 'u':
                    board[x-u][y] = 'u'
                    u += 1
                elif board[x-u][y] == 'q' or board[x-u][y] == 'p' or board[x-u][y] == 'k':
                    break
            else:
                break
        # 아래
        d = 1
        while True:
            if x+d<m:
                if board[x+d][y] == 0 or board[x+d][y] == 'u':
                    board[x+d][y] = 'u'
                    d+=1
                elif board[x+d][y] == 'q' or board[x+d][y] == 'p' or board[x+d][y] == 'k':
                    break
            else:
                break
        # 왼쪽
        l = 1
        while True:
            if y-l>=0:
                if board[x][y-l] == 0 or board[x][y-l] == 'u':
                    board[x][y-l] = 'u'
                    l+=1
                elif board[x][y-l] == 'q' or board[x][y-l] == 'p' or board[x][y-l] == 'k':
                    break
            else:
                break
        # 오른쪽
        r = 1
        while True:
            if y+r<n:
                if board[x][y+r] == 0:
                    board[x][y+r] = 'u'
                    r += 1
                elif board[x][y+r] == 'q' or board[x][y+r] == 'p' or board[x][y+r] == 'k':
                    break
            else:
                break

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans += 1
print(ans)