def draw_star(n):  # 별 찍는 곳은 1로 변경, 빈칸은 0 유지
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(a)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]


n = int(input())
Map = [[0 for i in range(n)] for j in range(n)]
draw_star(n)

for i in Map: # i 는 Map 의 행 기준 1치원 배열
    for j in i: # j 는 i 라는 배열 속 원소
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print() # 줄바꿈

