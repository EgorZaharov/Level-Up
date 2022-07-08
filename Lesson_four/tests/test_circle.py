from figures.circle import perimeter_circle, is_correct, square_circle
import pytest

def test_correct_perimeter():
    assert perimeter_circle(2) == 12.566370614359172

def test_correct_perimeter():
    assert square_circle(2) == 12.566370614359172

