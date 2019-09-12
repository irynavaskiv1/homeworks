# task
# Створіть скрипт, який би запитував у користувача значення змінної a,
# та змінної b, і після цього вивів на екран результати арифметичних операцій,
# над цими змінними.

variable_a = int(input('Please, enter a variable '))
variable_b = int(input('Please, enter b variable '))

plus = variable_a + variable_b
minus = variable_a - variable_b
multiply = variable_a * variable_b
share = variable_a / variable_b

print('a+b =', plus)
print('a-b =', minus)
print('a*b =', multiply)
print('a/b =', share)
