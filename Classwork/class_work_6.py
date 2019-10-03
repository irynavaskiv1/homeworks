class Figure:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def enter_the_sides(self):
        self.sides = [int(input("Enter side " + str(i + 1) + " : "))
                      for i in range(self.number_of_sides)]

    def show_side(self):
        for i in range(self.number_of_sides):
            print("Side", i+1, "is", self.sides[i])


class Rectangle(Figure):

    def __init__(self):
        super().__init__(2)

    def square(self):
        width, height = self.sides
        square = width * height
        print('The square of your figure is '.format(square))


class Square(Figure):

    def __init__(self):
        super().__init__(1)

    def square(self):
        side = self.sides
        square = side * 2
        print('The square of your figure is '.format(square))


r = Rectangle()
r.enter_the_sides()
r.show_side()
r.square()

s = Square()
s.enter_the_sides()
s.show_side()
s.square()
