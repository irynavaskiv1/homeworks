# task 2/a
a = int(input('Please, enter your number '))
a = int(a)

d1 = a % 10
d2 = a % 100 // 10
d3 = a // 100
print("Добуток цифр числа:", d1 * d2 * d3)

# task 2/b
my_list1 = [1, 2, 3, 4]
my_list1.reverse()
print('Числа в реверсному порядку', my_list1)

# task 2/c
my_list2 = [4, 3, 3, 2]
print('Посортовані цифри, що входять в число:', sorted(my_list2))
