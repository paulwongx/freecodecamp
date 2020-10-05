class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            print('Too big for the picture.')
            return "Too big for picture."

        pic = ''
        for r in range(self.height):
            pic += '*' * self.width + '\n'

        print(pic)
        return pic

    def get_amount_inside(self, guest_shape):
        home_area = self.get_area()
        guest_area = guest_shape.get_area()

        num_times = home_area // guest_area
        print(num_times)
        return num_times

    def __str__(self):
        output = f'Rectangle(width={self.width}, height={self.height})'
        print(output)
        return output


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self):
        output = f'Square(side={self.width})'
        print(output)
        return output


sq = Square(5)
sq.set_side(7)
print(sq)
sq.get_picture()