n = int(input())

def hanoi(n,a,b,c):
    global cnt
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

print(2**n-1)
hanoi(n,1,2,3)