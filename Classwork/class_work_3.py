def find_arefmet(*args):
    """This  function  finds arithmetic mean any number of numbers."""
    return sum(args) / len(args)
print(find_arefmet(12, 14))

# ------------------------------------------------------------------


def find_absolyt(arg):
    """This function that returns the absolute value of a number"""
    if arg > 0:
        return arg
    elif arg == 0:
        return arg
    else:
        return -arg


print(find_absolyt(-4))


def find_absolyt_second(arg):
    """This function that returns the absolute value of a number"""
    if arg > 0:
        return arg
    elif arg == 0:
        return arg
    else:
        return abs(arg)


print(find_absolyt_second(-4))

# ------------------------------------------------------------------


def max_value(*arg):
    """This function  finds the maximum number of two numbers,
    and also use the DocStrings documentation lines in the function."""
    return max(arg)


print(max_value(4, 6))


def max_value_second(a, b):
    """This function  finds the maximum number of two numbers,
    and also use the DocStrings documentation lines in the function."""
    if a > b:
        return a
    elif a < b:
        return a
    elif a == b:
        return print('These values are the same')
    else:
        print('I do not know your number')

# -----------------------------------------------------------------------


def area_rectangle(a, b):
    return a * b


def area_triangle(a, b, c):
    return (a + b + c) / 2


def area_circle(pi, a):
    pi = 3.14
    return pi * a


enter_shape = input('Enter for figure:')
"""This program that calculates the area of ​​a rectangle, triangle and circle
(write three functions to calculate the area and call them in the main
program depending on user choice)"""
if enter_shape == 'rectangle' or enter_shape == 'triangle' \
        or enter_shape == 'circle':
    while True:
        if enter_shape == 'rectangle':
            a = int(input("Please, enter first side: "))
            b = int(input("Please, enter second side: "))
            print('The area of the figure is', area_rectangle(a, b))
            break
        elif enter_shape == 'triangle':
            a = int(input("Please, enter first side: "))
            b = int(input("Please, enter second side: "))
            c = int(input("Please, enter third side: "))
            print('The area of the figure is', area_triangle(a, b, c))
            break
        elif enter_shape == 'circle':
            a = int(input("Please, enter the radius: "))
            pi = 3.14
            print('The area of the figure is', area_circle(pi, a))
            break
        else:
            print('I do not know your figure.')
else:
    print('Please, enter valid figure.')
print('The End!')

# ------------------------------------------------------------------------


def sum_digits(*args):
    """This function that calculates the sum of the digits of the number
    entered."""
    i = 0
    for variable in args:
        i = variable + i
    return i


print(sum_digits())

# -------------------------------------------------------------------------


def adding(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculator():
 """ First calculator program """
action = input('Please, enter your action: ')
while True:
    if action == 'adding':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(adding(a, b))
        break
    elif action == 'subtraction':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(subtraction(a, b))
        break
    elif action == 'multiplication':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(multiplication(a, b))
        break
    elif action == 'division':
        a = float(input('Please, enter your first number:  '))
        b = float(input('Please, enter your second number:  '))
        print(division(a, b))
        break
    else:
        print('I do not know your action')
calculator()
#  ---------------------------------------------------------


def calculator1():
    """ Second calculator program"""
    a = input('Please, enter first value: ')
    c = input('Please, enter your action: ')
    b = input('Please, enter second value: ')

    if c == '+':
        d = float(a) + float(b)
        print('Your result is ', d)
    elif c == '-':
        d = float(a) - float(b)
        print('Your result is ', d)
    elif c == '*':
        d = float(a) * float(b)
        print('Your result is ', d)
    elif c == '/':
        d = float(a) / float(b)
        print('Your result is ', d)
    else:
        print('I do not know :)')


calculator1()
