def search_values(x1, x2, discriminant):
    a = int(input("Введите коэффициент А:"))
    b = int(input("Введите коэффициент B:"))
    c = int(input("Введите коэффициент C:"))

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
    elif discriminant == 0:
        x1 = -b / (2 * a)
    return x1, x2, discriminant
