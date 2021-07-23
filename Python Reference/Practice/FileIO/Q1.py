# Find weather the poems.txt contains twinkle word

with open('D:\Programming\Python Reference\Practice\FileIO\poems.txt') as f:
    t = f.read()
    if 'twinkle' in t:
        print('Twinkle word is present in the Poem')
    else:
        print('Twinkle is not present')