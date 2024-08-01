class Point:
    """ A simple representation of a point in 2d space"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Instance of Point\n\n" + "\n".join([f"{k}: {v}" for k, v in self.__dict__.items()])

    def __add__(self, other):
        # here other is another instance of point
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # here other is another instance of point
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # here other is another instance of point
        return Point(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    point_one = Point(3, 2)
    print(point_one)
    print()
    point_two = Point(5, 3)
    print(point_two)
    print()
    point_three = point_one + point_two
    print(point_three)
    print()
    point_four = point_one - point_two
    print(point_four)
    print()
    point_five = point_one * point_two
    print(point_five)
    print()
    print(point_one == point_two)  # prints False
