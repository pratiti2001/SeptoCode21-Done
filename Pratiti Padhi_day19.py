t=int(input())
arr=[]
x=0
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    for j in range(n-1):
       if arr[j]==arr[j+1]:
           x+=1
    if x>=1:
        print("Gentle")
    else:
        print("Steep")
    x=0