import math
def is_correct(r):
    if r < 0:
        raise Exception("Error")

def perimeter_circle(r):
    is_correct(r)
    p = 2 * r * math.pi
    return p

def square_circle(r):
    is_correct(r)
    s = math.pi * (r ** 2)
    return s
