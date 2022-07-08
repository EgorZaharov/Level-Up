# from Lesson_four import sum_n
#
# def tests_sum_n():
#     assert sum_n(3,5) == 8
#
# def tests_sum_n2():
#     assert sum_n(3,5) == 8
#
# def tests_sum_n3():
#     assert sum_n(3,5) == 8

from Lesson_four import calendar_check
import pytest

def tests_input_digit():
    assert calendar_check(1) == 31

def tests_input_digit1():
    assert calendar_check(2) == 28

def tests_input_digit2():
    assert calendar_check(4) == 30

def tests_input_digit3():
    with pytest.raises(Exception): # проверка на ошибку
        calendar_check(13)
