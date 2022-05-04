from string import ascii_lowercase
alphabet=list(ascii_lowercase)

s=input()
arr=[]

buf=s.lower()

for i in alphabet:
    arr.append(buf.count(i))

max=arr.index(max(arr))
cnt=0
for j in range(len(arr)):
    if arr[j]==arr[max]:
        cnt+=1

if cnt>=2:
    print("?")
else:
    print(alphabet[max].upper())