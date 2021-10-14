a = input('Enter your name: ')
i = 0

while (i < len(a)):
    if a[i] == 'h' or a[i] == 'n':
        i = i + 1
        continue
    print(a[i])
    i = i + 1

