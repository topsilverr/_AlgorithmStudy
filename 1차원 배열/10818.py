def calc(arr):
    max=arr[0]
    min=arr[0]

    for i in arr:
        if i>max:
            max=i
        elif i<min:
            min=i

    print(min,max)
    # 그냥 print(min(arr),max(arr)) 해도 됨,,,,




n= int(input())
arr=[]
arr=list(map(int,input().split()))
calc(arr)


