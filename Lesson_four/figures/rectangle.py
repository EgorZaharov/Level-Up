def is_correct(a,b):
    if a < 0 or b < 0:
        raise Exception("Error")

def perimeter_rectangle(a,b):
    is_correct(a,b)
    p = (a + b) * 2
    return p

def square_rectangle(a,b):
    is_correct(a,b)
    s = a * b
    return s