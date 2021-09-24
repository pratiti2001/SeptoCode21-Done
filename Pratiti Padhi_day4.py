'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n = int(input())
list = []
for i in range(n):
    scores = int(input())
    list.append(scores)
for num in list:
    remainder = num % 5
    new = 5 - remainder
    if num <= 33:
        print(num)
    else:
        if new < 3:
            print(num + new)
        else:
            print(num)