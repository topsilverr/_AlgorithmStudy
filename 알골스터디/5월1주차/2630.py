n = int(input())

num=[]
blue = 0
white = 0

for i in range(n):
    num.append(list(map(int,input().split())))

def cutPaper(x,y,n):
    global blue
    global white
    now = num[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if now != num[i][j]:
                cutPaper(x,y,n//2)
                cutPaper(x+n//2,y,n//2)
                cutPaper(x+n//2,y+n//2,n//2)
                cutPaper(x,y+n//2,n//2)
                return
    if now == 0:
        white+=1
    else:
        blue+=1

cutPaper(0,0,n)
print(white)
print(blue)