t=int(input())
a=0
b=0
for i in range(t):
    n=int(input())
    arr=[]
    arr=[int(x) for x in input().split()]
    for j in range(n):
        if arr[j]%2==0:
            a+=1 
        else:
            b+=1 
    if a>n//2:
        for k in range(n):
            if arr[k]%2!=0:
                print(k+1)
    elif b>n//2:
        for l in range(n):
            if arr[l]%2==0:
                print(l+1)
    a=0
    b=0