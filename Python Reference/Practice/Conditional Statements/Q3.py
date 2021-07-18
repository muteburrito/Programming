# To check if the comment is spam

comment = input('Enter the comment: ').lower()
spam = False

if('make a lot of money' in comment):
    spam = True
elif('buy now' in comment):
    spam = True
elif('subscribe this' in comment):
    spam = True
elif('click this' in comment):
    spam = True
else:
    print('Comment is not a spam')

if spam == True:
    print('Comment is a spam')
else:
    pass