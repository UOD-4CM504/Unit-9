class Position:
    def __init__(self, x, y, x_upper, y_upper):
        self._x_upper = x_upper
        self._y_upper = y_upper
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        if self._x > self._x_upper:
            raise ValueError(f"x cannot be bigger than {self._x_upper}")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        if self._y > self._y_upper:
            raise ValueError(f"y cannot be bigger than {self._y_upper}")


if __name__ == "__main__":
    p = Position(0, 0, 10, 15)  # x=0, y=0,
    print(f"x={p.x} and y={p.y}")  # prints x=0 and y=0
    p.x = 2
    print(f"x={p.x} and y={p.y}")  # prints x=2 and y=0
    p.y += 3
    print(f"x={p.x} and y={p.y}")  # prints x=2 and y=3
    p.y += 13  # raises a ValueError