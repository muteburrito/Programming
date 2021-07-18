# Accept marks of 3 subjects and determine if the student has passed or not.
# Minimum criteria each subject 40 percent and total 40 percent to pass

sub1 = int(input('Enter marks of subject 1 out of 100: '))
sub2 = int(input('Enter marks of subject 2 out of 100: '))
sub3 = int(input('Enter marks of subject 3 out of 100: '))

subt = sub1+sub2+sub3
per = int(subt/ 3)

if (per >= 40) and (subt >= 99):
    print('You have passed')
else:
    print('You have failed')