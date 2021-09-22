'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
t=int(input("The no. of test cases="))
list=[]
for i in range(t):
    a,b=[int(x) for x in input("Enter the years:").split()]
    if a%4==0 and b%4==0:
        if a%100==0 and b%100==0:
            if a%400==0 and b%400==0:
                total_days= 732
            elif a%400==0 and b%400!=0:
                total_days= 731
            elif a%400!=0 and b%400==0:
                total_days= 731
            else:
                total_days= 730
        elif a%100==0 and b%100!=0:
            if a%400==0:
                total_days= 732
            else:
                total_days= 731
        elif a%100!=0 and b%100==0:
            if b%400==0:
                total_days= 732
            else:
                total_days= 731
        else:
            total_days= 732
    elif a%4==0 and b%4!=0:
        if a%100==0:
            if a%400==0:
                total_days= 731
            else:
                total_days= 730
        else:
            total_days= 731
    elif a%4!=0 and b%4==0:
        if b%100==0:
            if b%400==0:
                total_days= 731
            else:
                total_days= 730
        else:
            total_days= 731
    else:   
        total_days= 730
    list.append(total_days)
for z in range(t):
    print(list[z])