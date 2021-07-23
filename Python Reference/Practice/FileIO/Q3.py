def Game():
    return 74

score = Game()
with open('D:\Programming\Python Reference\Practice\FileIO\hiscore.txt', 'r') as f:
    hscore = int(f.read())

with open('D:\Programming\Python Reference\Practice\FileIO\hiscore.txt', 'w') as f:
    if hscore < score:
        f.write(str(score))
        print('You have set a new record')
    else:
        print('Try harder')
