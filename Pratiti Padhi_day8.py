t=int(input())
for n in range(t):
    string=str(input())
    l,u = 0,0
    for i in string:
        if (i>='a'and i<='z'):
            l=l+1                 
        if (i>='A'and i<='Z'):
            u=u+1
    if l>u:
        print(string.lower())
    elif l<u:
        print(string.upper())
    else:
        print(string.lower())