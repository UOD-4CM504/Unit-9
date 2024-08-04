class Position:
    pass


if __name__ == "__main__":
    p = Position(0, 0, 10, 10)  # x=0, y=0,
    print(f"x={p.x} and y={p.y}")  # prints x=0 and y=0
    p.x = 2
    print(f"x={p.x} and y={p.y}")  # prints x=2 and y=0
    p.y += 3
    print(f"x={p.x} and y={p.y}")  # prints x=2 and y=3
    p.x = 11  # raises ValueError: x cannot be bigger than 10
