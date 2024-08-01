import pytest
from Exercise import Position

def test_position_y_setter():
    p = Position(0, 0, 10, 8)
    p.y = 2
    assert p.y == 2
    p.y += 4
    assert p.y == 6
    with pytest.raises(ValueError, match='y cannot be bigger than 8'):
        p.y += 5

def test_position_x_setter():
    p = Position(0, 0, 10, 10)
    p.x = 2
    assert p.x == 2
    p.x += 4
    assert p.x == 6
    with pytest.raises(ValueError, match='x cannot be bigger than 10'):
        p.x += 5

@pytest.mark.parametrize("init_x, init_y, max_x, max_y, expected_x, expected_y", [
    (0, 0, 10, 10, 0, 0),
    (2, 3, 10, 10, 2, 3)
])
def test_position_initialization(init_x, init_y, max_x, max_y, expected_x, expected_y):
    p = Position(init_x, init_y, max_x, max_y)
    assert p.x == expected_x
    assert p.y == expected_y