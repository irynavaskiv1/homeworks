# task
# Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу i на &

zen = "Beautiful is better than ugly." \
      "Explicit is better than implicit." \
      "Simple is better than complex." \
      "Complex is better than complicated. " \
      "Flat is better than nested. " \
      "Sparse is better than dense. " \
      "Readability counts. " \
      "Special cases aren't special enough to break the rules. " \
      "Although practicality beats purity." \
      "Errors should never pass silently. " \
      "Unless explicitly silenced." \
      "In the face of ambiguity, refuse the temptation to guess. " \
      "There should be one-- and preferably only one --obvious way to do it." \
      "Although that way may not be obvious at first unless you're Dutch." \
      "Now is better than never." \
      "Although never is often better than *right* now." \
      "If the implementation is hard to explain, it's a bad idea." \
      "If the implementation is easy to explain, it may be a good idea." \
      "Namespaces are one honking great idea -- let's do more of those!"

# task 1/a
print(zen.count('better'))
print(zen.count('never'))
print(zen.count('is'))

# task 1/b
print(zen.upper())

# task 1/c
print(zen.replace('i', '&'))
