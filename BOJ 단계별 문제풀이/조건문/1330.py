def compare(a,b):
    if a>b:
        return ">"
    elif a<b:
        return "<"
    elif a==b:
        return "=="

a,b=map(int,input().split())
print(compare(a,b))