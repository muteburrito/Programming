secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('guess: ')
    # As we learned operators this will add 1 to the guess_count and store it.
    guess_count += 1
    # Here we converted the string into int to compare it with original number
    if int(guess) == secret_number:
        print('You win!')
        break  # This will break the loop
else:  # This is optional else statement for while loop
    print('You failed!')
