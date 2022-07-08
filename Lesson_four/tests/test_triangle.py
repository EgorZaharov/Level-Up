from figures.triangle import perimeter_triangle, is_correct, square_triangle
import pytest

def test_correct_perimeter():
    assert perimeter_triangle(2,3,4) == 9

def test_correct_square():
    assert square_triangle(2,3,4) == 2.9047375096555625

def test_correct_input():
    with pytest.raises(Exception):
        perimeter_rectangle(-2,-4,-6)