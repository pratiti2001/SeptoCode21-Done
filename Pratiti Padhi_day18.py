t=int(input())
balls=[]
a=0
b=[]
for i in range(t):
    n=int(input())
    balls=[int(x) for x in input().split()]
    for j in range(n):
        if j+1 not in balls:
            b.append(j+1)
            a+=1
    if a==0:
       print(0)
    else:
       print(*b)
    b=[]
    a=0
