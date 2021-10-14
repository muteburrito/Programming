a = input('Enter your name: ')

for letter in a:
    if letter == 'a' or letter == 'h':
        continue
    print(letter)