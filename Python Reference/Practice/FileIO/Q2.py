# Get a file path from usr and check if word dbrand is present

pth = input('Enter path of file: ')

with open(pth) as f:
    db = f.read()
    if 'dbrand' in db:
        print('Present')
    else:
        print('Absent')