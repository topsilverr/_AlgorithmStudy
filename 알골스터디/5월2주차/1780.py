# 3으로 나눈 값 ,,,

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int,input().split())))

minus_cnt = 0
zero_cnt = 0
one_cnt = 0

def cut_paper(x,y,n):
    global minus_cnt
    global zero_cnt
    global one_cnt
    now = p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if now != p[i][j]:
                cut_paper(x,y,n//3)
                cut_paper(x+n//3,y,n//3)
                cut_paper(x+2*(n//3),y,n//3)
                cut_paper(x,y+n//3,n//3)
                cut_paper(x,y+2*(n//3),n//3)
                cut_paper(x+n//3,y+n//3,n//3)
                cut_paper(x+n//3,y+2*(n//3),n//3)
                cut_paper(x+2*(n//3),y+n//3,n//3)
                cut_paper(x+2*(n//3),y+2*(n//3),n//3)
                return
    if now == 0:
        zero_cnt += 1
    elif now == 1:
        one_cnt += 1
    else:
        minus_cnt += 1

cut_paper(0,0,n)
print(minus_cnt)
print(zero_cnt)
print(one_cnt)
