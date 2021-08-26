# Get high score and if it higher write it in the file

def game():
    score = 102
    return score

yourscore = game()
with open('D:\Programming\Python Reference\Practice\hiscore.txt', 'r') as f:
    hiscore = int(f.read())

    if yourscore > hiscore:
        with open('D:\Programming\Python Reference\Practice\hiscore.txt', 'w') as f:
            f.write(str(yourscore))
        print('You made a high score')
    else:
        print('Try harder')
