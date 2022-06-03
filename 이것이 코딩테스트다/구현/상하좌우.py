n = int(input())
move = list(input().split())
arr = [[False for col in range(1, 101)] for row in range(1, 101)]  # 2차원 배열 false로 초기화
x, y = 1, 1  # 시작위치
now = [x, y]  # 현재위치
for i in range(1, n + 1):  # 주어진 칸들만 true로 변경
    for j in range(1, n + 1):
        arr[i][j] = True

for a in move:  # 주어진 방향들을 차례대로 진행
    if a == "R":
        y = y + 1
        if arr[x][y] == False:
            y = y - 1
    elif a == "L":
        y = y - 1
        if arr[x][y] == False:
            y = y + 1
    elif a == "U":
        x = x - 1
        if arr[x][y] == False:
            x = x + 1
    elif a == "D":
        x = x + 1
        if arr[x][y] == False:
            x = x - 1

print(x, y)
