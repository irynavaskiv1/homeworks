def solution(number):
    """Multiples of 3 or 5"""
    my_list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            my_list.append(i)
    return sum(my_list)
