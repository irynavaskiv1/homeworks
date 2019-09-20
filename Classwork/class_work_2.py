# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити
# серед них максимальне та  мінімальне число.

your_list = input('Ввведіть список: ')
print(max(your_list))
print(min(your_list))

# 2.  В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3.

my_list = range(1, 11)
for i in my_list:
    if i % 2 == 0:
      print(' в листі є парні значення')
else:
    print('кінець')


my_list = range(1, 11)
for i in my_list:
    if i % 3 == 0:
      print(' в листі є непарні значення')
else:
    print('кінець')


my_list = range(1, 11)
for i in my_list:
    if i % 3 != 0 and i % 2 != 0:
      print(' є значення, які не діляться на 2  і на 3')
else:
    print('кінець')

# 3.  Написати програму, яка обчислює факторіал числа,
# яке користувач вводить.(не використовувати рекурсивного виклику функції)

user_number = int(input('Enter your number: '))
factorial = 1

while user_number > 1:
    factorial *= user_number
    user_number -= 1
print(factorial)

# task 4
# Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

login_user = input('Enter your login: ')
login = 'First'
while login_user == login:
    print('Login is True, congrats!')
    break
else:
    print('Login is False, please try again, please!')
