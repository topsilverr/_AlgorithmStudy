x = int(input())

now = 0
chk = 0

while x > now:
    chk += 1
    now += chk

gap = now - x
if chk % 2 == 0:
    son = chk - gap
    mom = gap + 1
else:
    son = gap + 1
    mom = chk - gap

print(f'{son}/{mom}') # f-string 사용,,!
