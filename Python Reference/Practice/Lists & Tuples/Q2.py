# Write a program to accepts marks of 6 students and display them in a sorted manner

m1 = int(input('Enter marks of 1 student: '))
m2 = int(input('Enter marks of 2 student: '))
m3 = int(input('Enter marks of 3 student: '))
m4 = int(input('Enter marks of 4 student: '))
m5 = int(input('Enter marks of 5 student: '))
m6 = int(input('Enter marks of 6 student: '))
marksofsixtudents = [m1,m2,m3,m4,m5,m6]
marksofsixtudents.sort()
print(marksofsixtudents)