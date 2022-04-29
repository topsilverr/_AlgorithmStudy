n=input()
chk=0
while True:
    n1=n//10
    n2=n%10
    t=n1+n2
    buf=n2*10+(t%10)
    if buf==n:
        break
    chk=chk+1

print(chk)