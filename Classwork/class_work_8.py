# 1. Спробуйте переписати наступний код через map. Він приймає список реальних
# імен і замінює їх хеш-прізвищами, використовуючи  більш надійний
# метод-хешування.


names = ['Sam', 'Don', 'Daniel']
result = list(map(hash, names))
print(result)

# 2.  Вивести список кольору 'red', який найчастіше зустрічається в
# даному списку  ['red', 'green', 'black', 'red', 'brown', 'red', 'blue',
# 'red', 'red', 'yellow' ] використовуючи функцію filter.

color = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red',
         'red', 'yellow']


def colors(color1):
    if color1 == 'red':
        return color1
# print(list(filter(colors, color)))

# 3. Всі ці числа в списку мають стрічковий тип даних, наприклад
# [‘1','2','3','4','5','7'], перетворити цей список  в список, всі числа якого
# мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

from functools import partial


my_list = ['1', '2', '3', '4', '5', '7']

new = list(map(list, map(partial(map, int), my_list)))

# print(new)

my_list = ['1', '2', '3', '4', '5', '7']
new_list = list(map(int, my_list))
# print(new_list)


# 5.  Знайти найбільший елемент в списку  використовуючи функцію reduce


from functools import reduce


mylist = [1, 2, 3, 4, 5, 7]
cap_count = reduce(lambda a, x: a + x.count('tt'), mylist, 0)
# print(cap_count)

