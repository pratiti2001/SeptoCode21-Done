'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def Danger(inputstr,length):
    length=len(inputstr)
    count_0=0
    count_1=0
    for i in range(0,length-1):
        if(inputstr[i]=='0'):
            count_1=0
            count_0=count_0+1
        else:
            count_0=0
            count_1=count_1+1
        if (count_0>=6 or count_1>=6):
            return True
    return False
t=int(input())  
for j in range(t):
    n=int(input())
    s=input()[:n]
    if (Danger(s,n)):
        print("YES")
    else:
        print("NO")