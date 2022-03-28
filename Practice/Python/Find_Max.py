from pyparsing import nums


def find_max(numbers):
    max_num = float(0) # smaller than all other numbers
    for num in int(numbers):
        if num > max_num:
            num = max_num
            return max_num

find_max(numbers=15)