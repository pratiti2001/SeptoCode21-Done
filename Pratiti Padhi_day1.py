'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n=int(input("The no. of players="))
list=[]
for i in range(n):
    a,b,c=[int(x) for x in input("Enter scores of Level1, Level2, Level3:").split()]
    final_score=a+b*c/a-b
    list.append(final_score)
for z in range(n):
    print(list[z])
    