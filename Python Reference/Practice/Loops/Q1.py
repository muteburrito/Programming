# So in this project we will build a car game. The document and working of the game can be found in this folder
user_input = ''
started = False
stopped = False
while True:  # This means run the block of code unless we break it
    user_input = input('> ').lower()
    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
exit - to terminate the game''')
    elif user_input == 'start' and started == False:
        print('Car is started.. and ready to go!')
        started = True
        stopped = False
    elif user_input == 'start' and started == True:
        print('Car is already started')
    elif user_input == 'stop' and started == False:
        print('Car has not yet started! Please start the car')
    elif user_input == 'stop' and stopped == False:
        print('Car is stopped!')
        stopped = True
        started = False
    elif user_input == 'stop' and stopped == True:
        print('Car is already stopped')
    elif user_input == 'exit':
        break
    else:
        print("Sorry I don't get that!")
