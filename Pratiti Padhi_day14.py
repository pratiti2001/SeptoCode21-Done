t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    tallest=max(arr)
    index=arr.index(tallest)
    place=index+1
    print(place)