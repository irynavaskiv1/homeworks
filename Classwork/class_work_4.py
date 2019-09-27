
import pyowm

"""Weather for Lviv or other city"""
city = input('What city you are interested: ')
name = input('Tell me your name, please:  ')
owm = pyowm.OWM('746a74688b8215746bb43e716dd38854')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("Hello,  " + name + " the temperature in  " + city + " is " +
      str(temperature) + " for the Celsius. Also, the state of the sky is "
      + w.get_detailed_status() + ". Have a nice day!")


from random import randint


def iras_game():
    """First game with random number"""
    user_number = input("Please, guess the number ")
    program_number = randint(1, 100)
    while True:
        if int(user_number) == int(program_number):
            print('You guessed the number! Congrats!')
        elif int(user_number) < int(program_number):
            print('Your number is less')
            break
        elif int(user_number) > int(program_number):
            print('Your number is greater')
            break
        else:
            print('I do not know your number')


iras_game()

# Напишіть скрипт, який обчислює площу прямокутника a*b,
# площу трикутника 0.5*h*a, площу кола pi*r**2.
# (для виконання завдання необхідно імпортувати  модуль math,
# а з нього функцію pow() та значення змінної пі).

from math import pow

def calcutaling_area():
    figure = input("Please, enter your figure: ")
    if figure == "rectangle":
        a = input("Please enter first side ")
        b = input("Please enter second side ")
        print(a * b)
    elif figure == "triangle":
        a = input("Please enter first side ")
        h = input("Please enter height ")
        print(a * h * 0.5)
    elif figure == "circle":
        r = input("Please enter radius ")




calcutaling_area()

















