t=int(input())
for a in range(t):
    n=int(input())
    arr=[]
    for b in range(n):
        row = [int(i) for i  in input().split()]
        arr.append(row)
    csum=0
    for i in range(n):
        csum+=arr[i][-1]+arr[i][0]
    rsum=0
    for j in range(n):
        rsum+=arr[0][j]+arr[-1][j]
    if rsum>=csum:
        diff=rsum-csum
    else:
        diff=csum-rsum
    print(diff)    
        