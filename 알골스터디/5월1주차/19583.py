import sys
input = sys.stdin.readline

a, b, c = input().split()

start= set()
res = 0

# a_h, a_m = map(int, str(a).split(':'))
# b_h, b_m = map(int, str(b).split(':'))
# c_h, c_m = map(int, str(c).split(':'))

a = int(a[:2])*100 + int(a[3:])
b = int(b[:2])*100 + int(b[3:])
c = int(c[:2])*100 + int(c[3:])

while True:
    try:
        time, name = input().split()
        time = int(time[:2])*100 + int(time[3:])
        if time <= a:
            start.add(name)
        elif b <= time <= c:
            if name in start:
                res+=1
                start.remove(name)
    except:
        break
print(res)
