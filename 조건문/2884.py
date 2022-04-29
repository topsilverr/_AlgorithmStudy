def alarm(h, m):
    if m < 45:
        h = h - 1
        if h<0:
            h=23
        m = 60 - (45 - m)
    elif m >= 45:
        h = h
        m = m - 45
    print(h, m)


h, m = map(int, input().split())
alarm(h,m)
