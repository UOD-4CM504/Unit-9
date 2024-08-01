import pytest
from Exercise import Person

@pytest.mark.parametrize("first_name, surname, expected", [
    ("Joe", "Bloggs", "Bloggs, Joe"),
    ("Ada", "Lovelace", "Lovelace, Ada")
])
def test_format_name_comma(first_name, surname, expected):
    assert Person.format_name_comma(first_name, surname) == expected

@pytest.mark.parametrize("first_name, surname, age, expected_str", [
    ("Joe", "Bloggs", 27, "Bloggs, Joe"),
    ("Ada", "Lovelace", 36, "Lovelace, Ada")
])
def test_person_str_representation(first_name, surname, age, expected_str):
    p = Person(first_name, surname, age)
    assert str(p) == expected_str

@pytest.mark.parametrize("first_name, surname, age", [
    ("Joe", "Bloggs", 27),
    ("Ada", "Lovelace", 36)
])
def test_person_attributes(first_name, surname, age):
    p = Person(first_name, surname, age)
    assert p.first_name == first_name
    assert p.surname == surname
    assert p.age == age