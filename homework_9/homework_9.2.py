def sorter(*textbooks):
    """Fix the loop!"""
    return sorted(textbooks,  key=str.lower)


print(sorter('Algebra', 'Geometria', 'English', 'aldk'))