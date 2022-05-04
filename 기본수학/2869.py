import math

a,b,v=map(int,input().split())

now=(v-b)/(a-b)
print(math.ceil(now))