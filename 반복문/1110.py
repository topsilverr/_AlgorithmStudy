n=int(input())
buf=n
chk=0

while True:
    n1=buf//10
    n2=buf%10
    t=n1+n2
    buf=n2*10+(t%10)
    chk=chk+1
    if buf==n:
        break

print(chk)