def read_noons_input():
    x = int(input())
    y = int(input())
    z = input()
    return x, y, z

def calculate(x, y, z):
    if z == "+":
        print(f"{x} + {y} = {x + y}")
        return x + y

    elif z == "-":
        return x - y
    elif z == "/":
        return x / y
    elif z == "*":
        return x * y
