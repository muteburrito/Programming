metric = input('Press (L) for Pounds and (K) for Kilograms: ')
weight = input('Enter your weight: ')

if metric.upper() == 'K':
    converted_weight = int(weight) * 2.20462
    print(f'Your weight in Pounds is: {int(converted_weight)}')
elif metric.upper() == 'L':
    converted_weight = int(weight) * 0.453592
    print(f'Your weight in Kilograms is: {int(converted_weight)}')
else:
    print('Invalid Input')
null = input('Press any key to continue')
