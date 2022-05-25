def check(a,b,c):
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)

a,b,c=map(int,input().split())
check(a,b,c)