def summation(num):
    """Grasshopper - Summation"""
    suma = []
    for i in range(num+1):
        suma.append(i)
    return sum(suma)


print(summation(100))