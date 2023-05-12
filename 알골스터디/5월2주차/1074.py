n,r,c = map(int,input().split())

res = -1
reg = 0
start = 0 # 시작숫자,,,,
def z(x,y,n):
    global res
    global reg
    res+=1
    if n!= 1:
        for i in range(x,x+2**n):
            for j in range(y,y+2**n):
                z(x,y,n-1)
                z(x,y+2**(n-1),n-1)
                z(x+2**(n-1),y,n-1)
                z(x+2**(n-1),y+2**(n-1),n-1)
                return

    if n==1 and x <= r <= x+1 and y <= c <= y+1:
        for i in range(x):
            for j in range(y):
                if r == i and c == j:
                    print(4*(res-1) )



z(0,0,n)
