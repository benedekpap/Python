class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width (self, new_width):
        self.width = new_width

    def set_height (self, new_height):
        self.height = new_height

    def get_area (self):
        area = (self.width * self.height)

        return area

    def get_perimeter (self):
        perimeter = (2 * self.width + 2 * self.height)

        return perimeter

    def get_diagonal (self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)

        return diagonal

    def get_picture (self):
        if self.width < 50 and self.height < 50:
            output = ''
            for column in range(self.height):
                output = output + '*' * self.width + '\n'
            return output
        else:
            return ('Too big for picture.')

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

    def get_amount_inside(self, shape):
        fits = (self.get_area() / shape.get_area())

        return int(fits)


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, new_side_length):
        self.width = new_side_length
        self.height = new_side_length

    def __str__(self):
        return f'{self.__class__.__name__}(side={self.width})'

rect = Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
