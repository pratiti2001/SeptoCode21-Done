arr=[]
t=int(input())
for i in range(0,t):
    n=int(input())
    if n%2==0:
        for j in range(n//2):
            arr.append(2)
    else:
        arr.append(3)
        for k in range((n-3)//2):
            arr.append(2)
    print(len(arr))
    print(*arr)
    arr=[]