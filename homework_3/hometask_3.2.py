
# task 2/a
a = int(input('Please, enter your number '))
a = int(a)

d1 = a % 10
d2 = a % 100 // 10
d3 = a // 100
print("Добуток цифр числа:", d1 * d2 * d3)

# task 2/b
a = [1, 2, 3, 4]
print('Число в реверсному порядку:', reversed(a))

# task 2/c
a = [1, 2, 3, 4]
print('Посортовані цифри, що входять в число:', sorted(a))
