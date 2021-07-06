# temperature = input('Enter temperature in celcius')
#
# if int(temperature) < 30:
#     print("Its a cold day")
# elif int(temperature) > 30:
#     print("Its a hot day")
# else:
#     print("Its a pleasant day")
#
# # Here we also have !=, <=, >=

name = input('Enter your name: ')

if len(name) < 3:
    print('Your name is too short')
elif len(name) > 50:
    print('Your name is too big')
elif len(name) <= 49 and len(name) >= 4:
    print('Name looks promising')
else:
    print('Invalid Input')
