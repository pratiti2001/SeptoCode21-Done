t = int(input())
for x in range(t):
    string = input()
    count = 0
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            count += 1
        i += 1
    print(count)