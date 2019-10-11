class Person:
    """Classy Classes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.name + "'s age is " + str(self.age)

    def get_information(self):
        print(self.info)


p1 = Person('Iryna', 23)
p1.get_information()
