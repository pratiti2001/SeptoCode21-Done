count=0
t=int(input())
for i in range(t):
    n=int(input())
    while n>1:
        n//=2
        count+=1 
    print(count)
    count=0