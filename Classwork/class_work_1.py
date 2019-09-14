# 1.  Роздрукувати всі парні числа менші 100 (написати два варіанти коду:
# один використовуючи цикл while, а інший з використанням циклу for).

# task1
for number in range(0, 99, 2,):
    print(number, end=' ')

# task2
number = 2
while number < 100:
    number += 2
    print(number, end=' ')

# 2.  Роздрукувати всі непарні числа менші 100. (написати два варіанти коду:
# один використовуючи оператор continue, а інший без цього оператора).

# task2/1
for number in range(1, 99, 2):
    print(number, end=' ')

# task2/1
for number in range(1, 99, 2):
    print(number, end=' ')
    continue

# пробую з while
number = 0
while number < 100:
    print(number, end=' ')
    number += 1

# пробую while and continue
number = 1
while number <100:
    print(number)
    number += 2

# 3.  Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list:
    if i % 2 == 1:
        print('there are odd numbers')
        break
    else:
        print('no odd numbers in list')

# 4.  Створити список, який містить елементи цілочисельного типу,
# потім за допомогою циклу перебору змінити тип даних елементів на числа з
# плаваючою крапкою.  (Підказка: використати вбудовану функцію float ()).

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for a in my_list:
   my_list[i] = float(a)
   print(my_list)
   i += 1

# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи
# цикли.
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

n1 = 0
n2 = 1
i = 0
while i < 10:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1

# 6.  Створити список, що складається з чотирьох елементів типу string.
# Потім, за допомогою циклу for, вивести елементи по черзі на екран.

a = ['1', '2', '3', '4']
for i in a:
    print(i)

# 7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при
# виводі додавався певний символ, наприклад “#”.
#           (Підказка: цикл for може бути вкладений в інший цикл,
#           а також  треба використати функцію print(“ ”, end=”%”)).

a = ['1', '2', '3', '4']
for i in a:
    print(i, end='ira ')

# 8.  Юзер вводить число з клавіатури, написати скріпт, який визначає
# чи це число просте чи складне.

number = int(input('User, please enter your number: '))
if number == 1:
    print('Since the number 1 has only one divisor,'
          ' it is neither considered as simple nor complex. ')
elif number % 1 == 0 and number % number == 0 and \
        number % 2 == 0 or number % 3 == 0 or number % 4 == 0 or \
        number % 5 == 0 or number % 6 == 0 or number % 7 == 0 or \
        number % 8 == 0 or number % 9 == 0:
    print('This is a compound number.')
elif number % 1 == 0 and number % number == 0:
    print('This is a prime number.')
else:
    print('I do not know you number')
print('Thank you for using our software program! ')
