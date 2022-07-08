def is_correct(a,b,c):
    if a < 0 or b < 0 or c < 0:
        raise Exception("Error")

def perimeter_triangle(a,b,c):
    is_correct(a,b,c)
    p = a + b + c
    return p

def square_triangle(a,b,c):
    is_correct(a,b,c)
    x = (a + b + c) / 2
    s = (x * (x - a) * (x - b) * (x - c))**0.5
    return s