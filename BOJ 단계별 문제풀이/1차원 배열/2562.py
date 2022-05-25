arr=[]
for i in range(9):
    arr.append(int(input()))

max=max(arr)
index=arr.index(max)

print(max)
print(index+1)