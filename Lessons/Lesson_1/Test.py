import pytest
from unittest.mock import patch
from Exercise import Person

def mock_input_func(*args):
    return None

def mock_print_func(*args, **kwargs):
    pass

@pytest.fixture
def person():
    return Person()

@patch('builtins.input', side_effect=mock_input_func)
@patch('builtins.print', side_effect=mock_print_func)
def test_person_wave(mock_print, mock_input, person):
    person.wave()
    mock_print.assert_called_once_with('Hi, I am a person and I am waving!')