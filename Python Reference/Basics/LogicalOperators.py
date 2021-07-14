# Logical operator can be used in processing multiple conditions like eg-

good_score = True
bad_score = False

if good_score and bad_score:
    print("You Are eligible")
elif good_score or bad_score:
    print("You are not eligible")
elif good_score or not bad_score:
    print("You are not eligible")


# AND : Both must be true to comply the condition
# OR : Either of the one must be true
# NOT : Inverts the original
