n = int(input())

num = []

for i in range(n):
    num.append(list(map(int,input())))


def quardTree(x, y, n):
    now = num[x][y]
    for i in range(x, x + n): # x가 위아래 y 가 양옆 즉 행 열 순서
        for j in range(y, y + n):
            if now != num[i][j]:
                print('(', end='')
                quardTree(x, y, n // 2)
                quardTree(x, y + n // 2, n // 2)
                quardTree(x + n // 2, y, n // 2)
                quardTree(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if now == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return


quardTree(0, 0, n)
