# task
# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = int(input('Enter first number '))
b = int(input('Enter second number '))
a, b = b, a

print('First number is', a)
print('Second number is', b)
