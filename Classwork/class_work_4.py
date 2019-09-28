
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
    while True:
        program_number = randint(1, 100)
        user_number = input("Please, guess the number ")
        if user_number == 'quit':
            break
        if int(user_number) == int(program_number):
            print('You guessed the number! Congrats!')
        elif int(user_number) < int(program_number):
            print('Your number is less')
        elif int(user_number) > int(program_number):
            print('Your number is greater')
        else:
            print('I do not know your number')


iras_game()


def iras_game_second():
    """Second game with random number"""
    while True:
        try:
            number = int(input("Please, guess the number "))
            randNumber = randint(1, 100)
            if number == randNumber:
                print("Equal")
            elif number < randNumber:
                print("less")
            else:
                print("greater")
        except:
            break

iras_game_second()


import math


def calculation_area():
    """Script for calculation area"""
    while True:
        try:
            figure = input("Please, enter your figure: ")
            if figure == "rectangle":
                a = int(input("Please enter first side "))
                b = int(input("Please enter second side "))
                rectangle_area = (b * a)
                print('Your area is ', rectangle_area)
                break
            elif figure == "triangle":
                c = int(input("Please enter first side "))
                d = int(input("Please enter height "))
                triangle_area = c * d * 0.5
                print('Your area is ', triangle_area)
                break
            elif figure == "circle":
                r = int(input("Please enter radius "))
                pi = math.pi
                circle_area = pi * r **2
                print('Your area is ', circle_area)
                break
        except:
            break


calculation_area()
