t=int(input())
list=[]
if t>=1 and t<=10:
    for i in range(t):
        n=int(input())
        if n>=1 and n<=40 :
            temp=input()
            lst = [int(i) for i in temp.split(" ")]
            list.append(lst)
    for j in list: 
        output=[]   
        for i in j:
            if i>=1 and i<=40 and j.count(i) == 1:
                output.append(i)
        if output==[]:
            print("0")
        else:
            for j in output:
                print(j, end=" ")
            print()




