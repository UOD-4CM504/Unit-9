class Point:
    """ A simple representation of a point in 2d space"""
    pass


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
    print(point_one == point_two)
