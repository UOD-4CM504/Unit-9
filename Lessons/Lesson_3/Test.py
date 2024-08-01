import pytest
from Exercise import Point


def test_point_equality():
    p1 = Point(2, 5)
    p2 = Point(2, 6)
    p3 = Point(3, 5)
    p4 = Point(2, 5)
    assert p1 != p2
    assert p1 != p3
    assert p1 == p4
    assert p2 != p3


@pytest.mark.parametrize("p1, p2, expected_x, expected_y", [
    (Point(2, 5), Point(6.1, 5.1), 2 - 6.1, 5 - 5.1),
    (Point(2, 5), Point(-2, -1), 2 - (-2), 5 - (-1))
])
def test_point_subtraction(p1, p2, expected_x, expected_y):
    result = p1 - p2
    assert result.x == pytest.approx(expected_x)
    assert result.y == pytest.approx(expected_y)


@pytest.mark.parametrize("p1, p2, expected_x, expected_y", [
    (Point(2, 5), Point(6.1, 5.1), 2 * 6.1, 5 * 5.1),
    (Point(2, 5), Point(-2, -1), 2 * -2, 5 * -1)
])
def test_point_multiplication(p1, p2, expected_x, expected_y):
    result = p1 * p2
    assert result.x == pytest.approx(expected_x)
    assert result.y == pytest.approx(expected_y)


@pytest.mark.parametrize("p1, p2, expected_x, expected_y", [
    (Point(2, 5), Point(6.1, 5.1), 8.1, 10.1),
    (Point(2, 5), Point(-2, -1), 0, 4)
])
def test_point_addition(p1, p2, expected_x, expected_y):
    result = p1 + p2
    assert result.x == pytest.approx(expected_x)
    assert result.y == pytest.approx(expected_y)


@pytest.mark.parametrize("x, y, expected_str", [
    (2, 5, "Instance of Point\n\nx: 2\ny: 5"),
    (6.1, 5.1, "Instance of Point\n\nx: 6.1\ny: 5.1")
])
def test_point_str_representation(x, y, expected_str):
    p = Point(x, y)
    assert str(p) == expected_str


@pytest.mark.parametrize("x, y", [
    (2, 5),
    (6.1, 5.1)
])
def test_point_attributes(x, y):
    p = Point(x, y)
    assert p.x == pytest.approx(x)
    assert p.y == pytest.approx(y)
