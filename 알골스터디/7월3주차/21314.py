import sys

input = sys.stdin.readline

mk = input().rstrip()

min = ""
max = ""

chk = 0

for i in mk:
    if i == "M":
        chk += 1
    else:
        if chk > 0:
            min += str(10**chk + 5)
            max += str(5*(10**chk))
        else:
            min += '5'
            max += '5'
        chk = 0
if chk>0:
    max += '1'*chk
    min += str(10**(chk-1))

print(max)
print(min)