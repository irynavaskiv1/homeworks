# 1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає
# чи це число парне чи непарне, чи введені дані коректні.


def multiply_or_not():
    """Program with your number"""
    while True:
        try:
            number = int(input("Please, enter the number: "))
            if number <= 0:
                print('You must enter positive number')
            elif number % 2 == 0:
                print("multiply")
            elif number % 2 != 0:
                print("not multiply")
            else:
                print("I do not know you number")
        except Exception:
            print('you should enter number')


# multiply_or_not()

# 2.Напишіть програму, яка пропонує користувачу ввести свій вік, після чого
# виводить повідомлення про те чи вік є парним чи непарним числом. Необхідно
# передбачити можливість введення від’ємного числа, в цьому випадку згенерувати
# власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє
# введену інформацію.


def users_age():
    """Program with your number"""
    while True:
        try:
            age = int(input("Please, enter the age: "))
            if age <= 0:
                raise ValueError('That is not positive number')
            elif age % 2 == 0:
                print("multiply")
            elif age % 2 != 0:
                print("not multiply")
            else:
                print("I do not know you age")
        except ZeroDivisionError:
            break
# users_age()


# 3.Напишіть програму для обчислення частки двох чисел, які вводяться
# користувачем послідовно через кому, передбачити випадок ділення на нуль,
# випадки  синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finally.


def fraction():
    inp = list(map(int, input('Please, enter two numbers: ').split(',')))
    if inp == inp[0] and inp[1]:
        try:
            result = inp[0] / inp[1]
            print('Your division is:', result)
        except ZeroDivisionError:
            print("division by zero!")
        except ValueError:
            print("Should be int")
        finally:
            print("End of the program")
    else:
        print("Your should enter two numbers")


# fraction()

# 4.Написати  програму, яка аналізує введене число та в залежності від числа
# видає день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок
# і т.д.) . Врахувати випадки введення чисел від 8 і більше, а також випадки
# введення не числових даних.


def weekday():
    inp = input('Please, enter day of week: ')
    if inp == str(inp):
        try:
            if inp == 'Monday':
                print('Your day of week is:', inp)
            elif inp == 'Tuesday':
                print('Your day of week is:', inp)
            elif inp == 'Wednesday':
                print('Your day of week is:', inp)
            elif inp == 'Thursday':
                print('Your day of week is:', inp)
            elif inp == 'Friday':
                print('Your day of week is:', inp)
            elif inp == 'Saturday':
                print('Your day of week is:', inp)
            elif inp == 'Sunday':
                print('Your day of week is:', inp)
        except SyntaxError:
            print("Please enter the number correctly!")
        except ValueError:
            print("Should be in a word")
        finally:
            print("End of the program")
    else:
        print("Your should enter in a word")


# weekday()


class Week:
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return repr(self.day)


def weekday_second():
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
            5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    day = int(input('Please, enter day of week: '))
    days.get(day)
    if day <= 0 or day >= 8:
        return print('Your day is', days[day])
    else:
        raise Exception(' ')


while True:
    try:
        weekday_second()
        break
    except ValueError:
        print('Your should enter number from1 to 7')
        break
    finally:
        print("End of program")
