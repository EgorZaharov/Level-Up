from figures.rectangle import perimeter_rectangle, is_correct, square_rectangle
import pytest

def test_correct_perimeter():
    assert perimeter_rectangle(2,3) == 10

def test_correct_perimeter():
    assert square_rectangle(2,3) == 6