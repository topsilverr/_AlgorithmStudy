n, r, c = map(int, input().split())

res = 0


def z(x, y, N):
    global res

    if r == x and c == y:
        print(int(res))
        exit(0)
    if not (x <= r < x + N and y <= c < y + N):
        res += N * N
        return

    z(x, y, N / 2)
    z(x, y + N / 2, N / 2)
    z(x + N / 2, y, N / 2)
    z(x + N / 2, y + N / 2, N / 2)

z(0, 0, 2 ** n)
