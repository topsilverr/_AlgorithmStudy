def select(x,y):
    if x>0:
        if y>0:
            print("1")
        elif y<0:
            print("4")
    elif x<0:
        if y>0:
            print("2")
        elif y<0:
            print("3")

x=int(input())
y=int(input())
select(x,y)