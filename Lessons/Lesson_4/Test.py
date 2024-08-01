import pytest
from Exercise import Circle

@pytest.mark.parametrize("radius", [30, 10])
def test_circle_circumference(radius):
    c = Circle(radius)
    expected_circumference = 2 * 3.14159 * radius
    assert c.circumference() == pytest.approx(expected_circumference)

@pytest.mark.parametrize("radius", [30, 10])
def test_circle_area(radius):
    c = Circle(radius)
    expected_area = 3.14159 * radius**2
    assert c.area() == pytest.approx(expected_area)

def test_circle_pi():
    assert Circle.pi == pytest.approx(3.14159)

@pytest.mark.parametrize("radius", [30, 10])
def test_circle_radius(radius):
    c = Circle(radius)
    assert c.radius == radius