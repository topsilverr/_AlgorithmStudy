import sys

n=int(input())
items=list(map(int,input().split()))
items.sort()

m=int(input())
target=list(map(int,input().split()))

def binary_search(list,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if list[mid]==target:
        return list[mid]
    elif list[mid]<target:
        return binary_search(list,target,mid+1,end)
    elif list[mid]>target:
        return binary_search(list,target,start,mid-1)
for t in target:
    res=binary_search(items,t,0,n-1)
    if res != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')