# The best way to open and close the file is the 'with statement' so we have no need to open and close the file manually

with open('D:\Programming\Python Reference\Intermediate\ another.txt', 'r') as f:
    a = f.read()
    print(a)
# this is same as the older open and close just we have no need to close the file and follow this syntax:
# with open('file', 'mode') as variable_name:

